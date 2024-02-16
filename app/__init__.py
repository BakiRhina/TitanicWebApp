from flask import Flask
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    # Configuration, extensions, and other setup can be done here

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
