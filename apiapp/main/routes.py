from flask import Blueprint, render_template

from ..extensions import mongo

api_keys = mongo.db.api_keys

main = Blueprint('main', __name__)

@main.route('/')
def index():
    api_keys.insert_one({'text' : 10})
    return render_template('index.html')
