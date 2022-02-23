from aiogram import types

from data.texts import continue_button_text

continue_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text=continue_button_text['continue'])
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

