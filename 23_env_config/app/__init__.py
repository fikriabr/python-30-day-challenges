from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
