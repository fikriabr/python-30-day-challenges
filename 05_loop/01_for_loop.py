# For loop 
# Example 1: Basic for loop
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in fruits:
  print(fruit)  # Output: apple, banana, cherry, date, elderberry 

# Example 2: For loop with range
for i in range(5):
  print(i)  # Output: 0, 1, 2, 3, 4

# Example 3: For loop with index
for index in range(len(fruits)):
  print(f"Index {index}: {fruits[index]}")  # Output: Index 0: apple, Index 1: banana, etc.

# Example 4: For loop with enumerate
for index, fruit in enumerate(fruits):
  print(f"Index {index}: {fruit}")  # Output: Index 0: apple, Index 1: banana, etc.

# Example 5: Nested for loop
for i in range(3):
  for j in range(2):
    print(f"i: {i}, j: {j}")  # Output: i: 0, j: 0; i: 0, j: 1; i: 1, j: 0; etc.

# Example 6: For loop with a condition
for fruit in fruits:
  if 'a' in fruit:
    print(f"{fruit} contains 'a'")  # Output: apple contains 'a', banana contains 'a', date contains 'a'

# Example 7: For loop with break
for fruit in fruits:
  if fruit == 'cherry':
    print("Found cherry, breaking the loop.")
    break  # Stops the loop when 'cherry' is found
  print(fruit)  # Output: apple, banana

# Example 8: For loop with continue
for fruit in fruits:
  if fruit == 'banana':
    print("Skipping banana.")
    continue  # Skips the rest of the loop for 'banana'
  print(fruit)  # Output: apple, skipping banana, cherry, date, elderberry

# Example 9: For loop with else
for fruit in fruits:
  print(fruit)  # Output: apple, banana, cherry, date, elderberry
else:
  print("Finished iterating through the fruits.")  # Output: Finished iterating through the fruits.

# Example 10: For loop with a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
  print(f"Number: {number}")  # Output: Number: 1, Number: 2, etc.  

# Example 11: For loop with a string
for char in "Hello":
  print(f"Character: {char}")  # Output: Character: H, Character: e, etc.

# Example 12: For loop with a dictionary
student_info = {
  "name": "Andi",
  "age": 25,
  "is_graduated": True
}
for key, value in student_info.items():
  print(f"{key}: {value}")  # Output: name: Andi, age: 25, is_graduated: True

# Example 13: For loop with a set
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
  print(f"Unique Number: {number}")  # Output: Unique Number: 1, Unique Number: 2, etc.

# Example 14: For loop with a tuple
coordinates = (10.0, 20.0)
for coordinate in coordinates:
  print(f"Coordinate: {coordinate}")  # Output: Coordinate: 10.0, Coordinate: 20.0

# Example 15: For loop with a range and step
for i in range(0, 10, 2):
  print(f"Even Number: {i}")  # Output: Even Number: 0, Even Number: 2, etc.  
