# To execute this file
# python -m migrations.seeds.seed_task

from app import create_app, db
from app.models.task_model import Task
from datetime import datetime

app = create_app()

with app.app_context():
  if not Task.query.first():
    tasks = [
      Task(title="Belajar Flask", description="Latihan model & migrasi", is_done=False, created_at=datetime.utcnow()),
      Task(title="Belajar SQLAlchemy", description="Coba bikin model lain", is_done=False, created_at=datetime.utcnow()),
    ]
    db.session.add_all(tasks)
    db.session.commit()
    print("Seeder Task berhasil dijalankan.")
  else:
    print("Data sudah ada, skip insert.")