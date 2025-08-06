from flask import Blueprint
from app.controllers.user_controller import user_list

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users')
def list_users():
  return user_list()