from flask import Flask
from dotenv import load_dotenv
import os

from .main.routes import main
from .extensions import mongo

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = MONGO_URI

    mongo.init_app(app)

    app.register_blueprint(main)
    return app

app = create_app()
