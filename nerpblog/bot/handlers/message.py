from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.utils.deep_linking import decode_payload
from datetime import datetime
from nerpblog.app.services import UserServices
from nerpblog.app.services import PostServices
from nerpblog.app.services import CommentServices
from nerpblog.app.schemas.comment import AddComment

from nerpblog.bot.config import menu_keyboard, post_menu_keyboard
from nerpblog.bot.state import Post, Comment, EditProfile

from nerpblog.app.uow import UnitOfWork
uow = UnitOfWork()

router = Router()

@router.message(CommandStart(deep_link=True))
async def handler_deep_link(message: Message, command: CommandObject, state: FSMContext):
    await state.clear() 
    if await UserServices(uow).get_user(tgid=message.chat.id):
        ...
    else:
        await UserServices(uow).login(tgid=message.chat.id, name=message.chat.first_name, tglink=message.chat.username if message.chat.username else 'none')
        await message.answer(f'''nerp.blog\n\nВы успешно зарегистрировались!🎉''')
    args = command.args
    payload = decode_payload(args)
    if 'postid' in payload:
        try: 
            postid = int(payload.split('postid')[1])
        except ValueError:
            return
        p = await PostServices(uow).one_post(id=postid)
        if not p: await message.answer('Пост не найден(', reply_markup=menu_keyboard());return
        await message.answer(p.htmltext, parse_mode=ParseMode.HTML)
        if p.media:
            media_group = []
            for i in p.media:
                media_group.append(InputMediaPhoto(media=i))
            await message.answer_media_group(media_group)
        await state.set_state(Comment.post)
        await state.set_data({'postid':p.id})
        try:
            p.date = datetime.strptime(str(p.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
        except ValueError:
            p.date = datetime.strptime(str(p.date), "%Y-%m-%d %H:%M:%S").strftime("%H:%MD%d.%m")
        await message.answer(f'<b>Название:</b> {p.title}\n<b>Лайков:</b> {p.likes}\n<b>Дата:</b> {p.date}', reply_markup=post_menu_keyboard(p.id), parse_mode=ParseMode.HTML)
    return

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear() 
    if await UserServices(uow).get_user(tgid=message.chat.id):
        await message.answer(f'''nerp.blog\n\nВы уже зарегистрированы!🎉''')
    else:
        await UserServices(uow).login(tgid=message.chat.id, name=message.chat.first_name, tglink=message.chat.username if message.chat.username else 'none')
        await message.answer(f'''nerp.blog\n\nВы успешно зарегистрировались!🎉''')
    await message.answer('Меню 🏡', reply_markup=menu_keyboard())

@router.message(Comment.comment, F.content_type.in_([ContentType.TEXT]))
async def add_comment_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('postid'): return
    await CommentServices(uow).add_comment(AddComment(text=message.text, postid=data['postid'], tgid=message.chat.id))
    await message.answer('Ваш комментарий опубликован', reply_markup=post_menu_keyboard(data['postid']))


@router.message(Post.text, F.content_type.in_([ContentType.PHOTO]))
async def post_text_media(message: Message, album: list[Message], state: FSMContext):
    if not message.caption: return
    file_ids = []
    media_group = []
    for msg in album:
        file_id = msg.photo[-1].file_id
        file_ids.append(file_id)
        media_group.append(InputMediaPhoto(media=file_id, caption=msg.caption))
    data = await state.get_data()
    await state.set_state(Post.overview)
    data['plain'] = message.caption
    data['html'] = message.caption
    data['media'] = file_ids
    await state.set_data(data)
    k = [
            [
                InlineKeyboardButton(text='Опубликовать 🌐', callback_data='publish')
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
    await message.answer(f'<b>Шаг 3 <u>из</u> 3</b>\nНазвание: {data["title"]}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))


@router.message(Post.text, F.content_type.in_([ContentType.TEXT]))
async def post_text_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['plain'] = message.text
    data['html'] = message.html_text
    data['media'] = None
    await state.set_state(Post.overview)
    await state.set_data(data)
    k = [
            [
                InlineKeyboardButton(text='Опубликовать 🌐', callback_data='publish')
            ],
            [
                InlineKeyboardButton(text='Отменить ❌', callback_data='menu')
            ]
        ]
    await message.answer(data["html"], parse_mode=ParseMode.HTML)
    await message.answer(f'<b>Шаг 3 <u>из</u> 3</b>\nНазвание: {data["title"]}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))


@router.message(Post.title, F.content_type.in_([ContentType.TEXT]))
async def post_title_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Post.text)
    await state.set_data({'title':message.text})
    await message.answer('<b>Шаг 2 <u>из</u> 3</b>\nНапишите текст поста\nвы можете использовать <b><u><i>разметку</i></u></b>, а также прикреплять фотографии', parse_mode=ParseMode.HTML)

@router.message(EditProfile.edit, F.content_type.in_([ContentType.TEXT]))
async def edit_profile_handler(message: Message, state: FSMContext) -> None:
    u = await UserServices(uow).rename(message.chat.id, message.text)
    if not u: await message.answer('Пользователь не найден(')
    k = [
        [InlineKeyboardButton(text='Изменить имя ✏️', callback_data='edit_profile')],
        [InlineKeyboardButton(text='Мои посты 🗂', callback_data='posts')],
        [InlineKeyboardButton(text='Меню 🏡', callback_data='menu')]
    ]
    await message.answer(f'Профиль🧾\nИмя: {u.name}', reply_markup=InlineKeyboardMarkup(inline_keyboard=k))