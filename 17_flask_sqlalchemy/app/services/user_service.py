from app import db
from app.models.user_model import User

def get_all_users():
    return User.query.all()

def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user
