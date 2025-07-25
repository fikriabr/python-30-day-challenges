coordinate = (10, 20)
print (f"Coordinates: {coordinate}, Type: {type(coordinate)}")
# Tuple is immutable, so we cannot change its elements
# coordinate[0] = 15  # This will raise a TypeError   

# Example of tuple unpacking
x, y = coordinate
print(f"Unpacked Coordinates: x={x}, y={y}")
# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)