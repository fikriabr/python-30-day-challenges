from flask import request, jsonify
from app.services.user_service import get_all_users, create_user

def list_users():
  users = get_all_users()
  return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

def add_user():
  data = request.get_json()
  user = create_user(data["name"], data["email"])
  return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201
