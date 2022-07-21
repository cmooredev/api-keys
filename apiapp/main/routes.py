from flask import Blueprint, redirect, url_for, render_template, request

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
