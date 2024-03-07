from fastapi import APIRouter
from fastapi.responses import StreamingResponse, FileResponse, Response

from aiogram import Bot, exceptions
import io

from nerpblog.config import bot_token

mediaRouter = APIRouter(prefix='/media', tags=['media'])


@mediaRouter.get('/photo/{fileId}')
async def getMedia(fileId: str):
    bot = Bot(bot_token)
    try:
        async with  bot.context():  # or `bot.context()  bot.session`
            f = await bot.get_file(fileId)
            f = await bot.download_file(f.file_path)
        return Response(content=f.read(), media_type='image/png')
    except exceptions.TelegramBadRequest:
        return None


@mediaRouter.get('/cover.png')
async def getCover():
    return FileResponse('nerpblog/public/cover.png')