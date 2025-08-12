from flask import Blueprint
from app.controllers import post_controller

post_bp = Blueprint('post', __name__)

post_bp.route('/')(post_controller.index)
post_bp.route(
    '/post/new', methods=['GET', 'POST'])(post_controller.create)
post_bp.route(
    '/post/<int:post_id>/update', methods=['GET', 'POST'])(post_controller.update)
post_bp.route(
    '/post/<int:post_id>/delete', methods=['POST'])(post_controller.delete)
