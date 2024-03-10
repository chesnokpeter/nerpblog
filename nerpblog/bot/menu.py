from nerpblog.app.services import PostServices

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class MenuManager:
    def __init__(self, pservices: PostServices) -> None:
        self.services = pservices

    async def menu(self, offset: int, limit: int, **data) -> InlineKeyboardMarkup:
        back_menu = 'menu'
        list = await self.services.get_posts(offset=offset, limit=limit, **data)
        k = []
        l = False
        for i, v in enumerate(list):
            if not l:
                if len(list[i:]) >= 2:
                    k.append([InlineKeyboardButton(text=v.title, callback_data=f'postid{v.id}'), InlineKeyboardButton(text=list[i+1].title, callback_data=f'postid{list[i+1].id}')])
                    l = True
                else: k.append([InlineKeyboardButton(text=v.title, callback_data=f'postid{v.id}')])
            else: l = False
        if not k:
            k.append([InlineKeyboardButton(text='Посты не найдены', callback_data='empty')])
        elif len(list) < 6 and offset == 0:
            k.append([InlineKeyboardButton(text='Меню 🏡', callback_data=back_menu)])
        elif not k and offset != 0:
            k.append([InlineKeyboardButton(text='Посты не найдены', callback_data='empty')])
            k.append([InlineKeyboardButton(text='◀️', callback_data='back_post'), InlineKeyboardButton(text='Меню 🏡', callback_data=back_menu)])
        elif len(list) < 5:
            k.append([InlineKeyboardButton(text='◀️', callback_data='back_post'), InlineKeyboardButton(text='Меню 🏡', callback_data=back_menu)])
        elif not offset <= 0:
            k.append([InlineKeyboardButton(text='◀️', callback_data='back_post'), InlineKeyboardButton(text='Меню 🏡', callback_data=back_menu), InlineKeyboardButton(text='▶️', callback_data='next_post')])
        else:
            k.append([InlineKeyboardButton(text='Меню 🏡', callback_data=back_menu), InlineKeyboardButton(text='▶️', callback_data='next_post')])
        return InlineKeyboardMarkup(inline_keyboard=k)


