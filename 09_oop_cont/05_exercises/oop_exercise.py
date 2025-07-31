class Book:
  def __init__(self, title):
    self.title = title
    self.available = True

  def __str__(self):
    return f"Book: {self.title}, {self.available}"
