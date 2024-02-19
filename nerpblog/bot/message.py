from aiogram import Router, F, exceptions
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.deep_linking import decode_payload

from nerpblog.app.services import UserServices
from nerpblog.app.db.controller import UserController
from nerpblog.app.services import PostServices
from nerpblog.app.db.controller import PostController
from nerpblog.app.models import AddPost

from nerpblog.app.db import session
from nerpblog.bot.state import Post

ucontroller = UserController(session)
uservices =  UserServices(ucontroller)
pcontroller = PostController(session)
pservices = PostServices(pcontroller)

router = Router()

# @router.message(CommandStart(deep_link=True))  #! ТЕСТ
# async def handler(message: Message, command: CommandObject):
#     args = command.args
#     payload = decode_payload(args)
#     if 'postid' in payload:
#         try: 
#             postid = int(payload.split('postid')[0])
#         except Exception:
#             return
#         p = pservices.get_one_post(postid)
#         if not p: await message.answer('пост не найден')
#         if p['media']:
#             media_group = []
#             for i in p['media']:
#                 media_group.append(InputMediaPhoto(media=i))
#                 await message.answer_media_group(media_group)
#         await message.answer(f'<b>{p['title']}</b>\n{p['htmltext']}')
#         k = [
#                 [
#                     InlineKeyboardButton(text='Написать комментарий ✏️', callback_data='add_comm')
#                 ],
#                 # [
#                     # InlineKeyboardButton(text='Посмотреть комментарии 💬', callback_data='comments')
#                 # ],
#                 [
#                     InlineKeyboardButton(text='Меню 🏡', callback_data='menu')
#                 ]
#         ]
#         await message.answer(f'Лайков: {p['likes']}\n', reply_markup=InlineKeyboardMarkup(inline_keyboard=k))
#     return


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear() 
    if uservices.get_user(tgid=message.chat.id):
        await message.answer(f'''nerp.blog\n\nКажется, вы уже зарегистрированы!🎉''')
    else:
        uservices.login_user(tgid=message.chat.id, name=message.chat.first_name, tglink=message.chat.username)
        await message.answer(f'''nerp.blog\n\nВы успешно зарегистрировались!🎉''')
    k = [
            [
                InlineKeyboardButton(text='Создать пост 📝', callback_data='create')
            ],
            [
                InlineKeyboardButton(text='Посмотреть комментарии 💬 (Скоро!)', callback_data='comments')
            ],
            [
                InlineKeyboardButton(text='Мои посты 🗂 (Скоро!)', callback_data='posts')
            ]
        ]
    await message.answer('Меню 🏡', reply_markup=InlineKeyboardMarkup(inline_keyboard=k))

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
    await message.answer('Отлично, теперь напиши название твоего поста')

@router.message(Post.text, F.content_type.in_([ContentType.TEXT]))
async def post_title_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Post.title)
    await state.set_data({'plain':message.text,'html':message.html_text, 'media':None})
    await message.answer('Отлично, теперь напиши название твоего поста')

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


