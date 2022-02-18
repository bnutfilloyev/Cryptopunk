from aiogram import types
from aiogram.dispatcher import FSMContext

from data.texts import texts
from keyboards.inline.colour import choose_colour_button
from loader import dp
from states.States import Form
from utils.db_api.mongo import user_db


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo1_id'] = message.photo[-1].file_id
    await message.answer(texts['photo1'])
    await Form.Photo2.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Form.Photo2)
async def get_photo_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo2_id'] = message.photo[-1].file_id
    await message.answer(texts['photo2'])
    await Form.Photo3.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Form.Photo3)
async def get_photo_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo3_id'] = message.photo[-1].file_id

    user_db.insert_one({
        'id': message.from_user.id,
        'photo1_id': data['photo1_id'],
        'photo2_id': data['photo2_id'],
        'photo3_id': data['photo3_id'],
    })

    await message.answer(texts['change_background'], reply_markup=choose_colour_button)
    await state.finish()
