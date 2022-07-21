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
        return redirect(url_for("main.success", id=server_id))
    else:
        return render_template('purchase.html')

@main.route('/<id>')
def success(id):
    return render_template('success.html', id=id)

@main.route('/support')
def support():
    return render_template('support.html')

@main.route('/gen_api<id>')
def gen_api(id):
    api = generator(id)
    return redirect(url_for("success", id=api))
