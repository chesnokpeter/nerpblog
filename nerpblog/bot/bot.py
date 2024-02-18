import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher #Router, types, F, BaseMiddleware
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart, CommandObject
# from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from aiogram.utils.markdown import hbold, hitalic, hunderline 
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.utils.deep_linking import decode_payload
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.types import Message, InputMediaPhoto, InputMedia, ContentType as CT

from nerpblog.config import bot_token
from nerpblog.bot.middl import MediaMiddleware
from nerpblog.bot.message import router as messageRouter
from nerpblog.bot.inline import router as inlineRouter

dp = Dispatcher()
dp.message.middleware(MediaMiddleware())

dp.include_router(messageRouter)
dp.include_router(inlineRouter)


async def main() -> None:
    global bot
    bot = Bot(bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())