from flask import Blueprint, render_template
from dotenv import load_dotenv
import os
import pymongo
import secrets

main = Blueprint('main', __name__)

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/purchase')
def index():
    return render_template('purchase.html')

@main.route('/gen_api<id>')
def gen_api(id):
    mongodb_client = pymongo.MongoClient(MONGO_URI)
    db = mongodb_client["translatordb"]
    col = db["api_keys"]
    key = secrets.token_hex(16)
    server_key = {"id" : id}
    specs = {
            "id" : id,
            "key": key,
        }
    result = col.update_one(server_key ,{"$set":specs}, True)
    return render_template('index.html')
