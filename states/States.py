from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    Photo2 = State()
    Photo3 = State()
    Colour = State()
    GetComment = State()
    Payment = State()
    Confirm = State()
    SendGroup = State()
    GetID = State()
    GetPhoto = State()

