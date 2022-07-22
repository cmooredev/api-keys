from flask import Flask
#import talisman to force https
from flask_talisman import Talisman

from .main.routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    #wrap app with Talisman to force https
    Talisman(app, content_security_policy=None)
    return app

app = create_app()
