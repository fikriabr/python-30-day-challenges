from flask import Flask
from .extensions import db, login_manager
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")
    os.makedirs(app.instance_path, exist_ok=True)

    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import blueprint **setelah db di-init** untuk hindari circular import
    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Buat tabel
    with app.app_context():
        db.create_all()

    return app
