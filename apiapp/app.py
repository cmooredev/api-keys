from flask import Flask
#import talisman to force https
from flask_talisman import Talisman
from dotenv import load_dotenv
import os

from .main.routes import main

load_dotenv()
CSRF_KEY = os.getenv('CSRF_KEY')



def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    #wrap app with Talisman to force https
    Talisman(app, content_security_policy=None)
    app.config['SECRET_KEY'] = CSRF_KEY
    return app

app = create_app()
