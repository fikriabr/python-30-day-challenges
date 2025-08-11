from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app.models.user_model import User
from app.extensions import db


def register_user(username, email, password):
    if User.query.filter_by(username=username).first():
        return None, "Username already exists"
    if User.query.filter_by(email=email).first():
        return None, "Email already exists"

    hashed_pw = generate_password_hash(password, method="pbkdf2:sha256")
    new_user = User(username=username, email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return new_user, None


def login_user_service(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return user, None
    return None, "Invalid credentials"


def logout_user_service():
    logout_user()
