from calculator import add, subtract, multiply, divide

# Main Module
# This module uses the calculator module to perform arithmetic operations.

def main():
  print("Welcome to the Calculator Module!")
  
  # Example operations
  try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    return
  
  print(f"Addition: {a} + {b} = {add(a, b)}")
  print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
  print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
  
  try:
    print(f"Division: {a} / {b} = {divide(a, b)}")
  except ZeroDivisionError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
