class Shape:
  def draw(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def draw(self):
    return f"Drawing a Circle with radius {self.radius}"

class Square(Shape):
  def __init__(self, side_length):
    self.side_length = side_length

  def draw(self):
    return f"Drawing a Square with side length {self.side_length}"

def shape_factory(shape_type, size):
  if shape_type == "circle":
    return Circle(size)
  elif shape_type == "square":
    return Square(size)
  else:
    raise ValueError("Unknown shape type")
  
def main():
  circle = shape_factory("circle", 10)
  print(circle.draw())  # Output: Drawing a Circle with diameter 10
  
  square = shape_factory("square", 5)
  print(square.draw())    # Output: Drawing a Square with side length 5

if __name__ == "__main__":
  main()
