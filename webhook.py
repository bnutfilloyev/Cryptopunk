import stripe
from flask import Flask, jsonify, request

from data.config import ENDPOINT_SECRET
from handlers.users.stripe_confirm import confirm_stripe

endpoint_secret = ENDPOINT_SECRET

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
async def webhook():
    event = None
    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        await confirm_stripe(payment_intent)
    else:
        print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=8000)