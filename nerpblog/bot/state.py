from aiogram.fsm.state import State, StatesGroup

class Post(StatesGroup):
    text = State()
    title = State()
    overview = State()

class Comment(StatesGroup):
    post = State()
    comment = State()

class Pagination(StatesGroup):
    page = State()

class EditProfile(StatesGroup):
    edit = State()
