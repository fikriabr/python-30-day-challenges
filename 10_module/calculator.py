# Calculator Module
# This module provides basic arithmetic operations.

def add(a: float, b: float) -> float:
  """Returns the sum of a and b."""
  return a + b

def subtract(a: float, b: float) -> float:
  """Returns the difference of a and b."""
  return a - b

def multiply(a: float, b: float) -> float:
  """Returns the product of a and b."""
  return a * b

def divide(a: float, b: float) -> float:
  """Returns the quotient of a and b. Raises ValueError if b is zero."""
  if b == 0:
    raise ZeroDivisionError("Cannot divide by zero.")
  return a / b
