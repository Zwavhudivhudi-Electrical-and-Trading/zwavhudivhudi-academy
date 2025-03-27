from flask import Flask
from src.config import Config

def create_app():
    app = Flask(__name__)
    # app.config.from_object('Config')

    with app.app_context():
        from . import routes
        return app
