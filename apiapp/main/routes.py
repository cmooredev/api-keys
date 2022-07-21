from flask import Blueprint, redirect, url_for, render_template, request
from dotenv import load_dotenv
import os
import stripe
from .api import generator
from .payments import make_payment

load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')

main = Blueprint('main', __name__)

#----

def calculate_order_amount(items):
    return 1400

@main.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

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
