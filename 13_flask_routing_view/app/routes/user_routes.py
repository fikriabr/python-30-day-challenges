from flask import Blueprint
from app.controllers.user_controller import user_profile_page

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/<username>')
def user_profile(username):
  return user_profile_page(username)