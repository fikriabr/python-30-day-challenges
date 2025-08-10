from app import db
from app.models.task_model import Task

def create_task(data):
  new_task = Task(
    title = data.get("title"),
    description = data.get("description"),
    is_done = data.get("is_done", False)
  )
  db.session.add(new_task)
  db.session.commit()
  return new_task

def get_all_tasks():
  return Task.query.all()

def get_task(task_id):
  return Task.query.get(task_id)

def update_task(task_id, data):
  task = Task.query.get(task_id)
  if not task:
    return None
  task.title = data.get("title", task.title)
  task.description = data.get("description", task.description)
  task.is_done = data.get("is_done", task.is_done)
  db.session.commit()
  return task

def delete_task(task_id):
  task = Task.query.get(task_id)
  if not task:
    return None
  db.session.delete(task)
  db.session.commit()
  return task
  