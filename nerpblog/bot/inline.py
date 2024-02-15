from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from nerpblog.bot.state import Post
from nerpblog.bot.message import pservices, AddPost, uservices


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
        pservices.new_post(AddPost(htmltext=data['html'], title=data['title'], userid=uservices.get_user(tgid=callback.message.chat.id)[0].id, media=data['media']))
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