class Quote:
  def __init__(self, id, text, author):
    self.id = id
    self.text = text
    self.author = author

  def __str__(self):
    return f'"{self.text}" - {self.author} (ID: {self.id})'

  def to_dict(self):
    return {
      'id': self.id,
      'text': self.text,
      'author': self.author
    }
