from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.deep_linking import decode_payload

from datetime import datetime

from nerpblog.app.services import UserServices
from nerpblog.app.db.controller import UserController
from nerpblog.app.services import PostServices
from nerpblog.app.db.controller import PostController
from nerpblog.app.services import CommentServices
from nerpblog.app.db.controller import CommentController
from nerpblog.app.models import AddComment, AddPost

from nerpblog.bot.config import menu_keyboard, post_menu_keyboard

from nerpblog.app.db import session
from nerpblog.bot.state import Post, Comment

ucontroller = UserController(session)
uservices =  UserServices(ucontroller)
pcontroller = PostController(session)
pservices = PostServices(pcontroller)
ccontroller = CommentController(session)
cservices = CommentServices(ccontroller)

router = Router()

@router.message(CommandStart(deep_link=True))
async def handler_deep_link(message: Message, command: CommandObject, state: FSMContext):
    await state.clear() 
    if uservices.get_user(tgid=message.chat.id):
        ...
    else:
        uservices.login_user(tgid=message.chat.id, name=message.chat.first_name, tglink=message.chat.username)
        await message.answer(f'''nerp.blog\n\nВы успешно зарегистрировались!🎉''')
    args = command.args
    payload = decode_payload(args)
    if 'postid' in payload:
        try: 
            postid = int(payload.split('postid')[1])
        except ValueError:
            return
        p = pservices.get_one_post(postid)
        if not p: await message.answer('Пост не найден(', reply_markup=menu_keyboard());return
        await message.answer(p.htmltext, parse_mode=ParseMode.HTML)
        if p.media:
            media_group = []
            for i in p.media:
                media_group.append(InputMediaPhoto(media=i))
            await message.answer_media_group(media_group)
        await state.set_state(Comment.post)
        await state.set_data({'postid':p.id})
        p.date = datetime.strptime(str(p.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
        await message.answer(f'<b>Название:</b> {p.title}\n<b>Лайков:</b> {p.likes}\n<b>Дата:</b> {p.date}', reply_markup=post_menu_keyboard(), parse_mode=ParseMode.HTML)
    return

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear() 
    if uservices.get_user(tgid=message.chat.id):
        await message.answer(f'''nerp.blog\n\nКажется, вы уже зарегистрированы!🎉''')
    else:
        uservices.login_user(tgid=message.chat.id, name=message.chat.first_name, tglink=message.chat.username)
        await message.answer(f'''nerp.blog\n\nВы успешно зарегистрировались!🎉''')
    await message.answer('Меню 🏡', reply_markup=menu_keyboard())

@router.message(Comment.comment, F.content_type.in_([ContentType.TEXT]))
async def add_comment_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('postid'): return
    cservices.add_comment(AddComment(text=message.text, postid=data['postid'], tgid=message.chat.id))
    await message.answer('Ваш комментарий опубликован', reply_markup=post_menu_keyboard())


@router.message(Post.text, F.content_type.in_([ContentType.PHOTO]))
async def post_title_media(message: Message, album: list[Message], state: FSMContext):
    file_ids = []
    media_group = []
    for msg in album:
        file_id = msg.photo[-1].file_id
        file_ids.append(file_id)
        media_group.append(InputMediaPhoto(media=file_id, caption=msg.caption))
    await state.set_state(Post.title)
    await state.set_data({'plain':message.caption,'html':message.caption, 'media':file_ids})
    await message.answer('Напиши <b><u>название</u></b> твоего поста', parse_mode=ParseMode.HTML)

@router.message(Post.text, F.content_type.in_([ContentType.TEXT]))
async def post_title_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Post.title)
    await state.set_data({'plain':message.text,'html':message.html_text, 'media':None})
    await message.answer('Напиши <b><u>название</u></b> твоего поста', parse_mode=ParseMode.HTML)

@router.message(Post.title)
async def post_overview_handler(message: Message, state: FSMContext) -> None:
    if message.content_type == ContentType.TEXT:
        data = await state.get_data()
        data['title'] = message.text
        await state.set_state(Post.overview)
        await state.set_data(data)
        media_group = []
        k = [
                [
                    InlineKeyboardButton(text='Опубликовать 🌐', callback_data='publish')
                ],
                [
                    InlineKeyboardButton(text='Редактировать ✏️ (Скоро!)', callback_data='edit')
                ],
                [
                    InlineKeyboardButton(text='Отменить ❌', callback_data='menu')
                ]
            ]
        await message.answer(data["html"], parse_mode=ParseMode.HTML)
        if data['media']:
            media_group = []
            for i in data['media']:
                media_group.append(InputMediaPhoto(media=i))
            await message.answer_media_group(media_group)
        await message.answer(f'<b>Название:</b> {data["title"]}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))
    else:
        pass


