from flask import Flask
from flask_talisman import Talisman

from .main.routes import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    return app

Talisman(app, content_security_policy=None)

app = create_app()
