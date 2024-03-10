from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


def menu_keyboard() -> InlineKeyboardMarkup:
    k = [
        [
            InlineKeyboardButton(text='Создать пост 📝', callback_data='create')
        ],
        [
            InlineKeyboardButton(text='Мой профиль 🧾', callback_data='profile')
        ],
        [
            InlineKeyboardButton(text='Уведомления 📬 (Скоро!)', callback_data='notifications')
        ],
        [
            InlineKeyboardButton(text='Открыть сайт 🖥', web_app=WebAppInfo(url='https://nerp.blog'))
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=k)


def post_menu_keyboard(id:int) -> InlineKeyboardMarkup:
    k = [
            [
                InlineKeyboardButton(text='Написать комментарий ✏️', callback_data='add_comm')
            ],
            [
                InlineKeyboardButton(text='Посмотреть комментарии 💬', callback_data='list_comm')
            ],
            [
                InlineKeyboardButton(text='Открыть пост 🖥', web_app=WebAppInfo(url=f"https://nerp.blog/{id}"))
            ],
            [
                InlineKeyboardButton(text='Меню 🏡', callback_data='menu')
            ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=k)