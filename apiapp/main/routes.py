from flask import Blueprint, render_template
from dotenv import load_dotenv
import os
import pymongo

from apiapp.extensions import mongo

main = Blueprint('main', __name__)

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

@main.route('/')
def index():
    return render_template('index.html')
