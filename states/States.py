from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    Photo2 = State()
    Photo3 = State()
    GetComment = State()
    Payment = State()

