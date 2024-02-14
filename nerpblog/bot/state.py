from aiogram.fsm.state import State, StatesGroup

class Post(StatesGroup):
    text = State()
    title = State()
    overview = State()