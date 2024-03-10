from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.utils.deep_linking import decode_payload
from datetime import datetime
from nerpblog.app.services import UserServices
from nerpblog.app.services import PostServices
from nerpblog.app.services import CommentServices
from nerpblog.app.schemas.comment import AddComment

from nerpblog.bot.config import menu_keyboard, post_menu_keyboard
from nerpblog.bot.state import Post, Comment, EditProfile

from nerpblog.app.uow import UnitOfWork
uow = UnitOfWork()

router = Router()

@router.message(Command('help'))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear() 

    await message.answer('Если возникли проблемы, то можете написать главреду - @chesnokpeter\n/start')