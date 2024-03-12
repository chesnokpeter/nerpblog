from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, FileResponse, Response

from aiogram import Bot, exceptions
import io

from nerpblog.config import bot_token

mediaRouter = APIRouter(prefix='/media', tags=['media'])


@mediaRouter.get('/photo/{fileId}')
async def getMedia(fileId: str, request: Request):
    print(request.headers)
    print(request.client)
    bot = Bot(bot_token)
    try:
        async with  bot.context():  # or `bot.context()  bot.session`
            f = await bot.get_file(fileId)
            f = await bot.download_file(f.file_path)
        return StreamingResponse(io.BytesIO(f.read()), media_type='image/png')        
    except exceptions.TelegramBadRequest:
        return None


@mediaRouter.get('/cover.png')
async def getCover(request: Request):
    print(request.headers)
    print(request.client)
    return FileResponse('nerpblog/public/cover.png')