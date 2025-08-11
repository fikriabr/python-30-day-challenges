from flask import request, jsonify
from flask_login import login_required, current_user
from app.services.auth_service import register_user, login_user_service, logout_user_service


def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    user, error = register_user(username, email, password)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "User registered successfully"}), 201


def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing fields"}), 400

    user, error = login_user_service(username, password)
    if error:
        return jsonify({"error": error}), 401

    return jsonify({"message": "Login successful"})


@login_required
def logout():
    logout_user_service()
    return jsonify({"message": "Logout successful"})


@login_required
def profile():
    return jsonify({
        "username": current_user.username,
        "email": current_user.email
    })
