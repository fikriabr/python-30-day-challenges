numbers = {1, 2, 3, 2, 4, 1, 5}
print(f"Unique Numbers: {numbers}, Type: {type(numbers)}")
# Set Operations
# Adding an element
numbers.add(6)
print(f"After adding 6: {numbers}")
# Removing an element
numbers.remove(2)
print(f"After removing 2: {numbers}")
# Checking membership
print(f"Is 3 in numbers? {3 in numbers}")
# Set union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(f"Union of set_a and set_b: {union_set}")
# Set intersection
intersection_set = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b: {intersection_set}") 
# Set difference
difference_set = set_a.difference(set_b)
print(f"Difference of set_a and set_b: {difference_set}")
# Set symmetric difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric difference of set_a and set_b: {symmetric_difference_set}")
# Set comprehension
squared_numbers = {x**2 for x in range(1, 6)}
print(f"Squared Numbers: {squared_numbers}, Type: {type(squared_numbers)}")
# Checking if a set is a subset or superset
set_c = {1, 2}
set_d = {1, 2, 3, 4, 5}
print(f"Is set_c a subset of set_d? {set_c.issubset(set_d)}")
print(f"Is set_d a superset of set_c? {set_d.issuperset(set_c)}")
# Clearing a set
numbers.clear()
print(f"After clearing, numbers: {numbers}, Type: {type(numbers)}")
# Creating an empty set
empty_set = set()
print(f"Empty Set: {empty_set}, Type: {type(empty_set)}")
# Set with mixed data types
mixed_set = {1, "Hello", 3.14, True}
print(f"Mixed Set: {mixed_set}, Type: {type(mixed_set)}")
