from flask import Blueprint
from app.controllers.user_controller import list_users, add_user

user_bp = Blueprint("user", __name__)

user_bp.route("/", methods=["GET"])(list_users)
user_bp.route("/", methods=["POST"])(add_user)
