from app.extensions import db, bcrypt
from app.models.user_model import User


def register_user(username, password):
    """Register new user."""
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def verify_user(username, password):
    """Verify username and password to login."""
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return user
    return None
