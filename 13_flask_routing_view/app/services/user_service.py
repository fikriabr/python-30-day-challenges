from app.models.user import User

# Simulasi database sederhana
def get_user_by_name(name):
  fake_db = [
    User(1, "John Doe", "john@example.com"),
    User(2, "Jane Doe", "jane@example.com"),
    User(3, "Alex Smith", "alex@example.com")
  ]
  for user in fake_db:
    if user.name.lower() == name.lower():
      return user.to_dict()
  return None
