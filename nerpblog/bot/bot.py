import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from nerpblog.config import bot_token
from nerpblog.bot.middl import MediaMiddleware
from nerpblog.bot.handlers.message import router as messageRouter
from nerpblog.bot.handlers.inline import router as inlineRouter
from nerpblog.bot.handlers.commands import router as commandRouter


dp = Dispatcher()
dp.message.middleware(MediaMiddleware())

dp.include_router(messageRouter)
dp.include_router(inlineRouter)
dp.include_router(commandRouter)


async def main() -> None:
    global bot
    bot = Bot(bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())