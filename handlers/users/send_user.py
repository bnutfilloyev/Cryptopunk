from aiogram import types
from aiogram.dispatcher import FSMContext

from data.texts import texts
from loader import dp, bot
from states.States import Form


@dp.message_handler(commands=['send_user'], state="*")
async def send_user(message: types.Message, state: FSMContext):
    await message.answer(text=texts['get_user_id'])
    await Form.GetID.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Form.GetID)
async def get_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
        await message.answer(text=texts['get_photo'])
        await Form.GetPhoto.set()

@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=Form.GetPhoto)
async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        await bot.send_photo(chat_id=data['user_id'], photo=data['photo'])
        await message.answer(text=texts['send_user'])
        await state.finish()
