from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# Redirect to login page if user not logged in
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
