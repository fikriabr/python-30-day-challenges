# Basic Operations in Python

# Arithmetic Operations
a = 10
b = 5
sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b
modulus_result = a % b
exponent_result = a ** b
floor_division_result = a // b

# Print results of arithmetic operations
print(f"Sum: {sum_result}")  # Output: 15
print(f"Difference: {difference_result}")  # Output: 5
print(f"Product: {product_result}")  # Output: 50
print(f"Quotient: {quotient_result}")  # Output: 2.0
print(f"Modulus: {modulus_result}")  # Output: 0
print(f"Exponent: {exponent_result}")  # Output: 100000
print(f"Floor Division: {floor_division_result}")  # Output: 2

# Comparison Operations
is_equal = (a == b)
is_not_equal = (a != b)
is_greater = (a > b)
is_less = (a < b)
is_greater_or_equal = (a >= b)
is_less_or_equal = (a <= b)

# Print results of comparison operations
print(f"Is Equal: {is_equal}") # Output: False
print(f"Is Not Equal: {is_not_equal}")  # Output: True
print(f"Is Greater: {is_greater}") # Output: True
print(f"Is Less: {is_less}") # Output: False
print(f"Is Greater or Equal: {is_greater_or_equal}") # Output: True
print(f"Is Less or Equal: {is_less_or_equal}") # Output: False

# Logical Operations
x = True
y = False
logical_and = x and y
logical_or = x or y
logical_not = not x

# Print results of logical operations
print(f"Logical AND: {logical_and}") # Output: False
print(f"Logical OR: {logical_or}")   # Output: True
print(f"Logical NOT: {logical_not}") # Output: False

# Assignment Operations
c = 20
c += 5  # c = c + 5
c -= 3  # c = c - 3
c *= 2  # c = c * 2
c /= 4  # c = c / 4
c %= 3  # c = c % 3
c **= 2  # c = c ** 2
c //= 2  # c = c // 2

# Print the final value of c after assignment operations
print(f"Final value of c: {c}")

# Identity Operations
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()
print(f"List1 is List2: {list1 is list2}")  # True, same object
print(f"List1 is List3: {list1 is list3}")  # False, different objects
print(f"List1 is not List2: {list1 is not list2}")  # False
print(f"List1 is not List3: {list1 is not list3}")  # True, different objects

# Membership Operations
my_list = [1, 2, 3, 4, 5]
print(f"2 in my_list: {2 in my_list}")  # True
print(f"6 in my_list: {6 in my_list}")  # False
print(f"2 not in my_list: {2 not in my_list}")  # False
print(f"6 not in my_list: {6 not in my_list}")  # True

# Bitwise Operations
bit_a = 5  # 0101 in binary
bit_b = 3  # 0011 in binary
bitwise_and = bit_a & bit_b  # 0001 in binary
bitwise_or = bit_a | bit_b   # 0111 in binary
bitwise_xor = bit_a ^ bit_b  # 0110 in binary
bitwise_not = ~bit_a  # Inverts all bits
bitwise_left_shift = bit_a << 1   # Shifts bits to the left
bitwise_right_shift = bit_a >> 1  # Shifts bits to the right

# Print results of bitwise operations
print(f"Bitwise AND: {bitwise_and}")  # Output: 1
print(f"Bitwise OR: {bitwise_or}")    # Output: 7
print(f"Bitwise XOR: {bitwise_xor}")  # Output: 6
print(f"Bitwise NOT: {bitwise_not}")  # Output: -6 (inverts all bits)
print(f"Bitwise Left Shift: {bitwise_left_shift}")    # Output: 10 (0101 becomes 1010)
print(f"Bitwise Right Shift: {bitwise_right_shift}")  # Output: 2 (0101 becomes 0010)

# Membership Operations with Strings
my_string = "Hello, World!"
print(f"'Hello' in my_string: {'Hello' in my_string}")  # True
print(f"'Python' in my_string: {'Python' in my_string}")  # False
print(f"'Hello' not in my_string: {'Hello' not in my_string}")  # False
print(f"'Python' not in my_string: {'Python' not in my_string}")  # True

# Membership Operations with Tuples
my_tuple = (1, 2, 3, 4, 5)
print(f"3 in my_tuple: {3 in my_tuple}")  # True
print(f"6 in my_tuple: {6 in my_tuple}")  # False
print(f"3 not in my_tuple: {3 not in my_tuple}")  # False
print(f"6 not in my_tuple: {6 not in my_tuple}")  # True

# Membership Operations with Dictionaries
my_dict = {"name": "Andi", "age": 25}
print(f"'name' in my_dict: {'name' in my_dict}")  # True
print(f"'age' in my_dict: {'age' in my_dict}")  # True

# Membership Operations with Sets
my_set = {1, 2, 3, 4, 5}
print(f"3 in my_set: {3 in my_set}")  # True
print(f"6 in my_set: {6 in my_set}")  # False
print(f"3 not in my_set: {3 not in my_set}")  # False
print(f"6 not in my_set: {6 not in my_set}")  # True

# Membership Operations with NoneType
my_none = None
print(f"my_none is None: {my_none is None}")  # True
print(f"my_none is not None: {my_none is not None}")  # False

# Membership Operations with Empty Values
empty_list = []
print(f"1 in empty_list: {1 in empty_list}")  # False
print(f"1 not in empty_list: {1 not in empty_list}")  # True
empty_string = ""
print(f"'a' in empty_string: {'a' in empty_string}")  # False
print(f"'a' not in empty_string: {'a' not in empty_string}")  # True
empty_tuple = ()
print(f"1 in empty_tuple: {1 in empty_tuple}")  # False
print(f"1 not in empty_tuple: {1 not in empty_tuple}")  # True
empty_dict = {} # Empty dictionary
print(f"'key' in empty_dict: {'key' in empty_dict}")  # False
print(f"'key' not in empty_dict: {'key' not in empty_dict}")  # True
empty_set = set()  # Empty set
print(f"1 in empty_set: {1 in empty_set}")  # False
print(f"1 not in empty_set: {1 not in empty_set}")  # True
