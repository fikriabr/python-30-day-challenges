from flask import Flask
from config import Config
from .extensions import db, bcrypt, login_manager
from .models.user_model import User


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Inisialisasi ekstensi dengan aplikasi
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Fungsi user_loader untuk Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import dan registrasi Blueprint
    from .routes.auth_routes import auth_bp
    from .routes.post_routes import post_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp)

    with app.app_context():
        db.create_all()  # Membuat tabel database jika belum ada

    return app
