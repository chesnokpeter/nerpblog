from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def menu_keyboard() -> InlineKeyboardMarkup:
    k = [
        [
            InlineKeyboardButton(text='Создать пост 📝', callback_data='create')
        ],
        [
            InlineKeyboardButton(text='Посмотреть комментарии 💬 (Скоро!)', callback_data='comments')
        ],
        [
            InlineKeyboardButton(text='Мои посты 🗂', callback_data='posts')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=k)


def post_menu_keyboard() -> InlineKeyboardMarkup:
    k = [
            [
                InlineKeyboardButton(text='Написать комментарий ✏️', callback_data='add_comm')
            ],
            [
                InlineKeyboardButton(text='Посмотреть комментарии 💬', callback_data='list_comm')
            ],
            [
                InlineKeyboardButton(text='Меню 🏡', callback_data='menu')
            ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=k)