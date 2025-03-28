from flask import Flask
from src.config import Config

def create_app():
    app = Flask(__name__)
    # app.config.from_object('Config')

    with app.app_context():

        from src.routes import home_bp
        app.register_blueprint(home_bp)
        return app


    