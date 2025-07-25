student_information = {
  "name": "Budi",
  "age": 20,
  "major": "Informatics"
}

print(student_information["name"])  # Accessing the value associated with the key "name"

# changing a value in the dictionary
student_information["age"] = 21
print(student_information["age"])  # Output: 21 

# adding a new key-value pair
student_information["graduated"] = False
print(student_information["graduated"])  # Output: False
print(student_information)


