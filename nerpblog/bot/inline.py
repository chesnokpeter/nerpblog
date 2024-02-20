from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from datetime import datetime

from nerpblog.bot.state import Post, Comment
from nerpblog.bot.message import pservices, AddPost, uservices, AddComment, cservices

from nerpblog.bot.config import menu_keyboard, post_menu_keyboard


router = Router()

@router.callback_query()
async def callbacks_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'create':
        await state.clear()
        await callback.answer()
        await state.set_state(Post.text)
        await callback.message.edit_text(f'''Отправь текст поста, <b>форматирование</b> <i><b>использовать</b></i> <u>можно</u>, фотографии <b><u>тоже</u></b>''', inline_message_id=callback.inline_message_id,  parse_mode=ParseMode.HTML)
    elif callback.data == 'menu':
        await state.clear()
        await callback.answer()
        await callback.message.edit_text('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())
    elif callback.data == 'publish':
        await callback.answer()
        data = await state.get_data()
        await state.clear()
        if not data: return
        if not data.get('html') and not data.get('title') and not data.get('media'):return
        pservices.new_post(AddPost(htmltext=data['html'], title=data['title'], userid=uservices.get_user(tgid=callback.message.chat.id)[0].id, media=data['media']))
        await callback.message.edit_text('<b>Пост опубликован!</b> 🎉\nСсылка: (Скоро!)', inline_message_id=callback.inline_message_id, parse_mode=ParseMode.HTML)
        await callback.message.answer('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=menu_keyboard())
    elif callback.data == 'add_comm':
        await callback.answer()
        data = await state.get_data()
        await state.set_state(Comment.comment)
        await state.set_data(data)
        await callback.message.answer('Напиши свой комментарий к посту')
    elif callback.data == 'list_comm':
        await callback.answer()
        data = await state.get_data()
        if not data.get('postid'): return
        comments = cservices.get_comments(postid=data['postid'])
        if not comments: await callback.message.answer('Комментарии не найдены :(', reply_markup=post_menu_keyboard())
        it = 0
        for i in comments:
            i.date = datetime.strptime(str(i.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
            await callback.message.answer(f'<u><b>{i.username}</b></u>\n{i.text}\n<b>{i.date}</b>', parse_mode=ParseMode.HTML, reply_markup=post_menu_keyboard()) if it + 1 == len(comments) else await callback.message.answer(f'<u><b>{i.username}</b></u>\n{i.text}\n<b>{i.date}</b>', parse_mode=ParseMode.HTML);it+=1
    else:
        await callback.answer()