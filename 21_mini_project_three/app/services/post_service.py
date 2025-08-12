from app.extensions import db
from app.models.post_model import Post


def get_posts_by_user(user_id):
    """Retrieves all posts belonging to a specific user."""
    return Post.query.filter_by(user_id=user_id).order_by(Post.date_posted.desc()).all()


def get_post_by_id(post_id):
    """Get a post by id."""
    return Post.query.get_or_404(post_id)


def create_post(title, content, user_id):
    """Create a new post."""
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return new_post


def update_post(post, title, content):
    """Update existing post."""
    post.title = title
    post.content = content
    db.session.commit()
    return post


def delete_post(post):
    """Delete a post."""
    db.session.delete(post)
    db.session.commit()
