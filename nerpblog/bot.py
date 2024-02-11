import sys
sys.path.append('../nerpblog')

import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.markdown import hbold, hitalic, hunderline 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.deep_linking import decode_payload
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from nerpblog.app.services import UserServices
from nerpblog.app.db.controller import UserController
from nerpblog.app.services import PostServices
from nerpblog.app.db.controller import PostController
from nerpblog.app.models import AddPost

from app.db import session
from nerpblog.config import bot_token

ucontroller = UserController(session)
uservices =  UserServices(ucontroller)
pcontroller = PostController(session)
pservices = PostServices(pcontroller)

dp = Dispatcher()

class Post(StatesGroup):
    text = State()
    title = State()
    overview = State()

@dp.message(CommandStart(deep_link=True))
async def handler(message: Message, command: CommandObject):
    args = command.args
    payload = decode_payload(args)
    await message.answer(f"Your payload: {payload}")

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext, command: CommandObject) -> None:
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


@dp.callback_query()
async def callbacks_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'create':
        await state.clear()
        await callback.answer()
        await state.set_state(Post.text)
        await callback.message.edit_text(f'''Теперь отправь текст поста, <b>форматирование</b> <i><b>использовать</b></i> <u>можно</u>\nНо пока что картинки использовать нельзя😢''', inline_message_id=callback.inline_message_id,  parse_mode=ParseMode.HTML)
    elif callback.data == 'menu':
        await state.clear()
        await callback.answer()
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
        await callback.message.edit_text('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))
    elif callback.data == 'publish':
        await callback.answer()
        data = await state.get_data()
        await state.clear()
        if not data: return
        pservices.new_post(AddPost(htmltext=data['html'], title=data['title'], userid=uservices.get_user(tgid=callback.message.chat.id)[0].id))
        await callback.message.edit_text('<b>Пост опубликован!</b> 🎉\nСсылка: (Скоро!)', inline_message_id=callback.inline_message_id, parse_mode=ParseMode.HTML)
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
        await callback.message.answer('Меню 🏡', inline_message_id=callback.inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))

    else:
        await callback.answer()

@dp.message(Post.text)
async def post_title_handler(message: types.Message, state: FSMContext) -> None:
    if message.content_type == ContentType.TEXT:
        await state.set_state(Post.title)
        await state.set_data({'plain':message.text,'html':message.html_text})
        await message.answer('Отлично, теперь напиши название твоего поста')
    else:
        await message.answer('Извините, но мы пока можем взаимодействовать только с текстом😢\nОтправьте пост еще раз')

@dp.message(Post.title)
async def post_overview_handler(message: types.Message, state: FSMContext) -> None:
    if message.content_type == ContentType.TEXT:
        data = await state.get_data()
        data['title'] = message.text
        await state.set_state(Post.overview)
        await state.set_data(data)
        k = [
                [
                    InlineKeyboardButton(text='Опубликовать 🌐', callback_data='publish')
                ],
                [
                    InlineKeyboardButton(text='Редактировать название ✏️ (Скоро!)', callback_data='edit_title')
                ],
                [
                    InlineKeyboardButton(text='Редактировать текст ✏️ (Скоро!)', callback_data='edit_text')
                ],
                [
                    InlineKeyboardButton(text='Выйти ❌', callback_data='menu')
                ]
            ]
        await message.answer(f'<b>Название:</b> {data["title"]}\n{data["html"]}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(inline_keyboard=k))
    else:
        pass

async def main() -> None:
    global bot
    bot = Bot(bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())