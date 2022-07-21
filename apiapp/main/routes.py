from flask import Blueprint, redirect, url_for, render_template, request, abort
from dotenv import load_dotenv
import os
import stripe
from .api import generator


load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')
STRIPE_PUBLIC = os.getenv('STRIPE_PUBLIC')
ENDPOINT_SECRET = os.getenv('ENDPOINT_SECRET')

main = Blueprint('main', __name__)

#----


@main.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    plan = request.form.get('plan')
    server_id = request.form.get('server_id')
    item = []
    if str(plan) == 'intro':
        item = [{
            'price': 'price_1LO3ZMBMA2F3juHIWj8p2PXM',
            'quantity': 1,
        }]
    elif str(plan) == 'basic':
        item = [{
            'price': 'price_1LO3uVBMA2F3juHIeLTSXoAq',
            'quantity': 1,
        }]
    elif str(plan) == 'pro':
        item =[{
            'price': 'price_1LO3vOBMA2F3juHI8WUwLgEm',
            'quantity': 1,
        }]
    try:
        checkout_session = stripe.checkout.Session.create(
            metadata={"server_id": server_id,
                    "plan": plan,
            },
            line_items=item,
            mode='payment',
            success_url=url_for('main.success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('main.pricing', _external=True),
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)
#----

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/success')
def success():
    return render_template('success.html', id=0, plan=1)

@main.route('/support')
def support():
    return render_template('support.html')

@main.route('/cancel')
def cancel():
    return render_template('cancel.html')

@main.route('/server_form', methods=['POST'])
def server_form():
    return render_template('server_form.html')

@main.route('/stripe_webhook', methods=['POST'])
def stripe_webhook():
    print('webhook called')
    if request.content_length > 1024 * 1024:
        print('request too big')
        abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = ENDPOINT_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        print('invalid payload')
        return {}, 400
    except stripe.error.SignatureVerificationError as e:
        print('invalid signature')
        return {}, 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        server_id = session['metadata']['server_id']
        plan = session['metadata']['plan']
        print(server_id)
        print(plan)
        api = generator(server_id, plan)
        print(f'new api key: {api}')
        ##line_items = stripe.checkout.Session.list_line_items(session="id")
        #print(line_items)
    return{}
