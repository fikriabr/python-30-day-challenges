# While Loop Example
# Example 1: Basic while loop
count = 0
while count < 5:
  print(f"Count is: {count}")  # Output: Count is: 0, 1, 2, 3, 4
  count += 1

# Example 2: While loop with a condition
number = 10
while number > 0:
  print(f"Number is: {number}")  # Output: Number is: 10, 9, 8, ..., 1
  number -= 1

# Example 3: While loop with break
count = 0
while True:
  if count == 3:
    print("Breaking the loop at count 3.")
    break  # Stops the loop when count is 3
  print(f"Count is: {count}")  # Output: Count is: 0, 1, 2
  count += 1

# Example 4: While loop with continue
count = 0
while count < 5:
  count += 1
  if count == 3:
    print("Skipping count 3.")
    continue  # Skips the rest of the loop for count 3
  print(f"Count is: {count}")  # Output: Count is: 1, Skipping count 3, Count is: 4, Count is: 5

# Example 5: While loop with else
count = 0
while count < 5:
  print(f"Count is: {count}")  # Output: Count is: 0, 1, 2, 3, 4
  count += 1
else:
  print("Finished iterating through the count.")  # Output: Finished iterating through the count.

# Example 6: While loop with a list
fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
  print(f"Fruit at index {index}: {fruits[index]}")  # Output: Fruit at index 0: apple, etc.
  index += 1
else:
  print("Finished iterating through the fruits list.")  # Output: Finished iterating through the fruits list.
