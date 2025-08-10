from flask import Blueprint
from app.controllers import task_controller

task_bp = Blueprint('tasks', __name__)

task_bp.route('/', methods=['POST'])(task_controller.create_task)
task_bp.route('/', methods=['GET'])(task_controller.get_tasks)
task_bp.route('/<int:task_id>', methods=['GET'])(task_controller.get_task)
task_bp.route('/<int:task_id>', methods=['PUT'])(task_controller.update_task)
task_bp.route('/<int:task_id>', methods=['DELETE'])(task_controller.delete_task)
