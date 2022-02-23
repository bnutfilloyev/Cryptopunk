from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.texts import texts
from keyboards.default.buttons import continue_button
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(texts['welcome_text'].format(message.from_user.full_name), reply_markup=continue_button)
