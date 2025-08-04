from flask import render_template
from app.services.user_service import get_user_by_name

def user_profile_page(username):
  user = get_user_by_name(username)
  if not user:
    return "User not found", 404
  return render_template('profile.html', user=user)