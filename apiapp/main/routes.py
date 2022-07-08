from flask import Blueprint, render_template

from apiapp.extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    api_keys = mongo.db.api_keys
    api_keys.insert_one({'text' : 10})
    return render_template('index.html')
