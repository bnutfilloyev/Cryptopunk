from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

from data.config import PRICE, GROUP_ID
from data.texts import texts, confirm_payment_button_text
from loader import dp, bot
from states.States import Form
from utils.db_api.mongo import user_db
from utils.stripe import create_link_stripe


@dp.callback_query_handler(state=Form.Colour)
async def change_colour(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['colour'] = call.data
        user_db.update_one({'id': call.from_user.id}, {
            "$set": {
                'colour': call.data
            }})

    await call.message.answer(texts['comment_message'])
    await Form.GetComment.set()


@dp.message_handler(state=Form.GetComment)
async def stripe(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        user_db.update_one({'id': msg.from_user.id}, {
            "$set": {
                'comment': msg.text
            }})
        data['comment'] = msg.text
        bot_name = dict(await bot.get_me())['username']

        link = await create_link_stripe(PRICE * 100, bot_name)
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=confirm_payment_button_text['subscribe'], url=link[0]),
            ]
        ])

        data['intenet_id'] = link[-1]
        data['payment_method'] = 'stripe'

        await msg.answer(text=texts['pay_text'].format(
            data['colour'],
            data['comment'],
            PRICE,
        ), reply_markup=pay_button)

        await state.finish()

        user_db.update_one({'id': msg.from_user.id},
                           {'$set': {
                               'intenet_id': str(data['intenet_id']),
                           }
                           })
