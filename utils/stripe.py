import stripe

from data.config import STRIPE, CHANEL
from loader import bot

stripe.api_key = STRIPE


async def create_link_stripe(amount, bot_name, currency, plan):

    data = stripe.Product.create(
        name="Gold Special",
        type="good",
        attributes=["size", "color"],
        metadata={
            "description": "This is a gold special",
            "display_sku": "gold-special",
            "display_price": f"{amount} {currency}",
            "display_currency": f"{currency}",
        },

    )

    price = stripe.Price.create(
        unit_amount=amount,
        currency=currency.lower(),
        product="prod_KyDBeasX5H30dU",
    )
    price = stripe.Price.create(
        unit_amount=amount,
        currency=currency.lower(),
        recurring={
            'interval': plan,
        },
        product=data.id,
        metadata={
            'display_name': 'Gold Special',
            'display_price': f"{amount} {currency}",
            'display_currency': f"{currency}",
        },
    )

    payment = stripe.checkout.Session.create(
        success_url=f"http://t.me/{bot_name}",
        cancel_url=f"http://t.me/{bot_name}",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    try:
        await bot.send_message(CHANEL, f"🤖@{bot_name}\n 💰<b>Payment</b>\n\n<code>{str(payment)}</code>")
    except Exception as ex:
        await bot.send_message(CHANEL, f"🤖@{bot_name}\n <code>{str(ex)}</code>")


    return [payment.url, payment.payment_intent]


async def check_status_stripe(intent_id):
    intent = stripe.PaymentIntent.retrieve(
        intent_id
    )
    try:
        await bot.send_message(CHANEL, f"<b>INTENT</b>\n<code>{str(intent)}</code>")
    except Exception as ex:
        await bot.send_message(CHANEL, f"<code>{str(ex)}</code>")


    return intent.status
