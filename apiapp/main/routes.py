from flask import Blueprint, redirect, url_for, render_template, request
from dotenv import load_dotenv
import os
import stripe
from .api import generator


load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')

main = Blueprint('main', __name__)

#----


@main.route('/create-checkout-session/<plan>', methods=['POST'])
def create_checkout_session(plan):
    item = []
    if str(plan) == 'intro':
        item = [{
            'price': 'price_1LO3ZMBMA2F3juHIWj8p2PXM',
            'quantity': 1,
        }]
    elif str(plan) == 'basic':
        item = [{
            'price': 'price_1LO3uVBMA2F3juHIeLTSXoAq',
            'quantity': 2,
        }]
    elif str(plan) == 'pro':
        item =[{
            'price': 'price_1LO3vOBMA2F3juHI8WUwLgEm',
            'quantity': 1,
        }]
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=item,
            mode='payment',
            success_url='https://hellabots.com/success',
            cancel_url='https://hellabots.com/pricing',
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

@main.route('/<id>#<plan>')
def success(id, plan):
    api = generator(id, plan)
    return render_template('success.html', id=api, plan=plan)

@main.route('/support')
def support():
    return render_template('support.html')

@main.route('/cancel')
def cancel():
    return render_template('cancel.html')
