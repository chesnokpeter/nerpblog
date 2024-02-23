import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
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