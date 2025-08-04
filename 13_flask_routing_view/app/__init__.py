from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.user_routes import user_bp
    from app.routes.main_routes import main_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)

    return app