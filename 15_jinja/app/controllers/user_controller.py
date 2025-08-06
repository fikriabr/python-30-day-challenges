from flask import render_template
from app.services.user_service import get_all_users

def user_list():
  users = get_all_users()
  return render_template("index.html", users=users)
