from flask import Blueprint, redirect, url_for, render_template, request
from dotenv import load_dotenv
import os
import stripe
from .api import generator


load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')

main = Blueprint('main', __name__)

#----

def calculate_order_amount(items):
    return 1400

@main.route('/create-checkout-session', methods=['POST', 'GET'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        line_items[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'translatoooor',
                },
                'uint_amount': 1,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://hellabots.com/success',
        cancel_url='https://hellabots.com/cancel',
    )
    return redirect(session.url, code=303)
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

@main.route('/purchase', methods=["POST", "GET"])
def purchase():
    if request.method =='POST':
        server_id = request.form['server_id']
        plan = request.form['plan']
        return redirect(url_for("main.success", id=server_id, plan=plan))
    else:
        return render_template('purchase.html')

@main.route('/<id>#<plan>')
def success(id, plan):
    api = generator(id, plan)
    return render_template('success.html', id=api, plan=plan)

@main.route('/support')
def support():
    return render_template('support.html')
