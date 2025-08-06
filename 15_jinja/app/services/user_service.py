from app.models.user_model import User

def get_all_users():
  return [
    User("John Doe", "johndoe@mail.com"),
    User("Jane Smith", "janesmite@mail.com"),
    User("Alice Johnson", "alice@mail.com"),
  ]