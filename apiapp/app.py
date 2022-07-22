from flask import Flask
from flask_talisman import Talisman

from .main.routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    Talisman(app, content_security_policy=None)
    return app



app = create_app()
