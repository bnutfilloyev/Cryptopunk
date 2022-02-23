import stripe

from data.config import STRIPE

stripe.api_key = STRIPE


async def create_link_stripe(amount, bot_name):
    data = stripe.Product.create(
        name="Gold Special",
        type="good",
        attributes=["size", "color"],
        metadata={
            "description": "This is a gold special",
            "display_sku": "gold-special",
            "display_price": f"{amount} USD",
            "display_currency": "USD",
        },

    )
    price = stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        product=data.id,
        metadata={
            'display_name': 'Gold Special',
            'display_price': f"{amount} USD",
            'display_currency': "USD",
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
        mode="payment",
    )
    return [payment.url, payment.payment_intent]

