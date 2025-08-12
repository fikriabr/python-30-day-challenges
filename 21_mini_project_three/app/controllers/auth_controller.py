from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.services import auth_service
from app.models.user_model import User


def register():
    if current_user.is_authenticated:
        return redirect(url_for('post.index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('auth.register'))
        auth_service.register_user(username, password)
        flash('Account successfully created! Please login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


def login():
    if current_user.is_authenticated:
        return redirect(url_for('post.index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = auth_service.verify_user(username, password)
        if user:
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('post.index'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    return render_template('auth/login.html')


def logout():
    logout_user()
    return redirect(url_for('auth.login'))
