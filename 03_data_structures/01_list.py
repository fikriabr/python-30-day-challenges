fruits = [ 'apple', 'banana', 'cherry', 'date', 'elderberry' ]
print(fruits[0])  # Accessing first item, start from index 0; Output: apple

# Manipulating items in the list
# Changing an item
fruits[1] = 'blueberry'  # Changing 'banana' to 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# Adding items to the list
fruits.append('grape')  # Adding 'grape' to the end of the list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'grape']

# Inserting an item at a specific position
fruits.insert(2, 'kiwi')  # Inserting 'kiwi' at index 2
print(fruits)  # Output: ['apple', 'blueberry', 'kiwi', 'cherry', 'date', 'elderberry', 'grape']  

# Deleting items from the list
# Using del to remove an item by index
del fruits[2]  # Deleting 'kiwi' at index 2
print(fruits)  # Output:  ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'grape']
# Using pop to remove the last item 
last_fruit = fruits.pop()  # Removes 'grape' and returns it
print(last_fruit)  # Output: grape
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# Using remove to delete an item by value
# Note: If the item is not found, it raises a ValueError
if 'date' in fruits:    # Check if 'date' is in the list before removing
    fruits.remove('date')  # Removing 'date' by value 
else:
    print("Item 'date' not found in the list.")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'elderberry']

