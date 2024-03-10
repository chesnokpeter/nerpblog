from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, InputMediaPhoto, InlineQuery
from aiogram.types.link_preview_options import LinkPreviewOptions
from aiogram.types.web_app_info import WebAppInfo
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from datetime import datetime
from nerpblog.bot.state import Post, Comment, Pagination, EditProfile
from nerpblog.bot.config import menu_keyboard, post_menu_keyboard
from nerpblog.bot.menu import MenuManager
from nerpblog.app.services import UserServices
from nerpblog.app.services import PostServices
from nerpblog.app.services import CommentServices
from nerpblog.app.uow import UnitOfWork
from nerpblog.app.schemas.post import AddPost
uow = UnitOfWork()

router = Router()

@router.callback_query(Pagination.page)
async def callbacks_handler_pagination(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    k = MenuManager(PostServices(uow))
    if not data.get('offset') == 0: 
        if not data.get('offset'): return
    if callback.data == 'next_post':
        data['offset'] += 6
        await state.set_data(data)
        u = await UserServices(uow).get_user(tgid=callback.message.chat.id)
        k = await k.menu(data['offset'], 6, userid=u.id)
        await callback.message.edit_text('Мои посты 🗂', reply_markup=k)
    elif callback.data == 'back_post':
        if data['offset'] <= 0:
            return
        data['offset'] -= 6
        await state.set_data(data)
        u = await UserServices(uow).get_user(tgid=callback.message.chat.id)
        k = await k.menu(data['offset'], 6, userid=u.id)
        await callback.message.edit_text('Мои посты 🗂', reply_markup=k)
    elif callback.data == 'menu':
        await state.clear()
        await callback.answer()
        await callback.message.edit_text('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())
    elif 'postid' in callback.data:
        try: 
            postid = int(callback.data.split('postid')[1])
        except ValueError:
            return
        p = await PostServices(uow).one_post(id=postid)
        if not p: await callback.message.answer('Пост не найден(', reply_markup=menu_keyboard());return
        await callback.message.answer(p.htmltext, parse_mode=ParseMode.HTML)
        if p.media:
            media_group = []
            for i in p.media:
                media_group.append(InputMediaPhoto(media=i))
            await callback.message.answer_media_group(media_group)
        await state.set_state(Comment.post)
        await state.set_data({'postid':p.id})
        try:
            p.date = datetime.strptime(str(p.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
        except ValueError:
            p.date = datetime.strptime(str(p.date), "%Y-%m-%d %H:%M:%S").strftime("%H:%MD%d.%m")
        await callback.message.answer(f'<b>Название:</b> {p.title}\n<b>Лайков:</b> {p.likes}\n<b>Дата:</b> {p.date}', reply_markup=post_menu_keyboard(p.id), parse_mode=ParseMode.HTML)

@router.callback_query(Post.overview)
async def callbacks_handler_post_overview(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    if callback.data == 'publish':
        data = await state.get_data()
        await state.clear()
        if not data: return
        if not data.get('html') and not data.get('title') and not data.get('media'):return
        u = await UserServices(uow).get_user(tgid=callback.message.chat.id)
        if not u: return
        p = await PostServices(uow).add_post(AddPost(htmltext=data['html'], title=data['title'], userid=u.id, media=data['media']))
        if not p: return
        await callback.message.edit_text(f'<b>Пост опубликован!</b> 🎉\nСсылка: <a href="https://nerp.blog/{p.id}">nerp.blog/{p.id}</a>', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Открыть пост 🖥', web_app=WebAppInfo(url=f"https://nerp.blog/{p.id}"))]]), inline_message_id=callback.inline_message_id, parse_mode=ParseMode.HTML, link_preview_options=LinkPreviewOptions(is_disabled=True))
        await callback.message.answer('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())
    elif callback.data == 'menu':
        await state.clear()
        await callback.message.edit_text('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())

@router.callback_query()
async def callbacks_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    if callback.data == 'create':
        await state.clear()
        await state.set_state(Post.title)
        await callback.message.edit_text(f'''<b>Шаг 1 <u>из</u> 3</b>\nНапишите название поста''', inline_message_id=callback.inline_message_id,  parse_mode=ParseMode.HTML)
    elif callback.data == 'menu':
        await state.clear()
        await callback.message.edit_text('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())
    elif callback.data == 'add_comm':
        data = await state.get_data()
        await state.set_state(Comment.comment)
        await state.set_data(data)
        await callback.message.answer('Напиши свой комментарий к посту')
    elif callback.data == 'list_comm':
        data = await state.get_data()
        if not data.get('postid'): return
        comments = await CommentServices(uow).get_comments(postid=data['postid'])
        if not comments: await callback.message.answer('Комментарии не найдены :(', reply_markup=post_menu_keyboard())
        it = 0
        for i in comments:
            i.date = datetime.strptime(str(i.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
            await callback.message.answer(f'<u><b>{i.username}</b></u>\n{i.text}\n<b>{i.date}</b>', parse_mode=ParseMode.HTML, reply_markup=post_menu_keyboard(data['postid'])) if it + 1 == len(comments) else await callback.message.answer(f'<u><b>{i.username}</b></u>\n{i.text}\n<b>{i.date}</b>', parse_mode=ParseMode.HTML);it+=1
    elif callback.data == 'posts':
        await state.clear()
        await state.set_state(Pagination.page)
        await state.set_data({"offset":0})
        k = MenuManager(PostServices(uow))
        u = await UserServices(uow).get_user(tgid=callback.message.chat.id)
        k = await k.menu(0, 6, userid=u.id)
        await callback.message.edit_text('Мои посты 🗂', reply_markup=k)
    elif callback.data == 'profile':
        await state.clear()
        u = await UserServices(uow).get_user(tgid=callback.message.chat.id)
        if not u: return
        k = [
            [InlineKeyboardButton(text='Изменить имя ✏️', callback_data='edit_profile')],
            [InlineKeyboardButton(text='Мои посты 🗂', callback_data='posts')],
            [InlineKeyboardButton(text='Меню 🏡', callback_data='menu')]
        ]
        await callback.message.edit_text(f'Профиль🧾\nИмя: {u.name}', reply_markup=InlineKeyboardMarkup(inline_keyboard=k))
    elif callback.data == 'edit_profile':
        await state.clear()
        await state.set_state(EditProfile.edit)
        await callback.message.edit_text('Введите ваше новое имя', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Отменить ❌', callback_data='menu')]]))



@router.inline_query()
async def handle_inline_query(inline_query: InlineQuery):
    print(inline_query)