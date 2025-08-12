from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.services import post_service


@login_required
def index():
    posts = post_service.get_posts_by_user(current_user.id)
    return render_template('posts/index.html', posts=posts)


@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_service.create_post(title, content, current_user.id)
        flash('Post created successfully!', 'success')
        return redirect(url_for('post.index'))
    return render_template('posts/create.html')


@login_required
def update(post_id):
    post = post_service.get_post_by_id(post_id)
    if post.author != current_user:
        abort(403)  # Forbidden
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_service.update_post(post, title, content)
        flash('Post updated successfully!', 'success')
        return redirect(url_for('post.index'))
    return render_template('posts/update.html', post=post)


@login_required
def delete(post_id):
    post = post_service.get_post_by_id(post_id)
    if post.author != current_user:
        abort(403)  # Forbidden
    post_service.delete_post(post)
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('post.index'))
