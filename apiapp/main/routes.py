from flask import Blueprint, render_template

from .api import generator

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/purchase')
def purchase():
    return render_template('purchase.html')

@main.route('/gen_api<id>')
def gen_api(id):
    api = generator(id)
    return render_template('purchase.html', text=api)
