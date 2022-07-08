from flask import Flask

from .main.routes import main
from .extensions import mongo


def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = MONGO_URI

    app.register_blueprint(main)
    return app

app = create_app()
