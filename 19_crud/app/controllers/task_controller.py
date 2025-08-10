from flask import jsonify, request
from app.services import task_service

def create_task():
  data = request.get_json()
  task = task_service.create_task(data)
  return jsonify({
    "message": "task created",
    "data": {
      "id": task.id, "title": task.title, "description": task.description, "is_done": task.is_done
    }
  }), 201

def get_tasks():
  tasks = task_service.get_all_tasks()
  return jsonify({
    "message": "get all task",
    "data": [{
      "id": task.id, "title": task.title, "description": task.description, "is_done": task.is_done
    } for task in tasks ]
  }), 201


def get_task(task_id):
  task = task_service.get_task_by_id(task_id)
  if not task:
    return jsonify({"error": "Task not found"}), 404
  return jsonify({
    "id": task.id, "title": task.title, "description": task.description, "is_done": task.is_done
  })

def update_task(task_id):
  data = request.get_json()
  task = task_service.update_task(task_id, data)
  if not task:
    return jsonify({"error": "Task not found"}), 404
  return jsonify({"message": "Task updated"})

def delete_task(task_id):
  task = task_service.delete_task(task_id)
  if not task:
    return jsonify({"error": "Task not found"}), 404
  return jsonify({"message": "Task deleted"})
