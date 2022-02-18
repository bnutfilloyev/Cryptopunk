from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose_colour_button = [
    [
        {
            "text": "🔵",
            "callback_data": "colour_red"
        }, {
            "text": "🟡",
            "callback_data": "colour_orange"
        }, {
            "text": "🟢",
            "callback_data": "colour_green"
        }
    ],
    [
        {
            "text": "🟣",
            "callback_data": "colour_blue"
        }, {
            "text": "🟠",
            "callback_data": "colour_purple"
        }, {
            "text": "🔴",
            "callback_data": "colour_black"
        }
    ]
]

choose_colour_button = InlineKeyboardMarkup(inline_keyboard=choose_colour_button)