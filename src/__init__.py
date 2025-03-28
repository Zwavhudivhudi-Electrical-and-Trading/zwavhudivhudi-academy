from flask import Flask
from src.config import Config

def create_app():
    app = Flask(
        __name__,
        template_folder="src/templates",  # Set templates folder
        static_folder="src/static"        # Set static folder
    )
    app.config.from_object(Config)  # Uncomment if needed

    with app.app_context():
        from src.routes import home_bp
        app.register_blueprint(home_bp)

    return app
