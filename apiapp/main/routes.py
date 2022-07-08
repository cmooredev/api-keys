from flask import Blueprint, render_template
from dotenv import load_dotenv
import os
import pymongo

main = Blueprint('main', __name__)

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/gen_api<id>')
def index(id):
    mongodb_client = pymongo.MongoClient(MONGO_URI)
    db = mongodb_client["translatordb"]
    col = db["api_keys"]
    specs = {
            "key" : id,
        }
    result = col.update_one({}, {'$set':specs}, True)
    return render_template('index.html')
