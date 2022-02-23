from aiogram.types.input_media import InputMediaPhoto

from data.config import GROUP_ID
from data.texts import texts
from loader import bot
from utils.db_api.mongo import user_db


async def confirm_stripe(payment_intent):
    intend_id = payment_intent['charges']['data'][0]['payment_intent']

    db_data = user_db.find_one_and_delete({'intenet_id': intend_id})

    await bot.send_message(db_data['id'], texts['pay_success'])

    await bot.send_media_group(
        GROUP_ID,
        [
            InputMediaPhoto(db_data['photo1_id']),
            InputMediaPhoto(db_data['photo2_id']),
        ]
    )

    await bot.send_message(GROUP_ID, texts['send_group_text'].format(
        db_data['id'],
        db_data['colour'],
        db_data['comment'],
    ))
