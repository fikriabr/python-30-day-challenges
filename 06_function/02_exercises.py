# Excercise Functions with List and Dictionaries

# Function to print student information
def print_student_info(students):
  for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Example usage of the print_student_info function
students = [
  {"name": "Andi", "age": 25, "major": "Computer Science"},
  {"name": "Budi", "age": 20, "major": "Informatics"},
  {"name": "Cici", "age": 22, "major": "Mathematics"}
]
print_student_info(students)

# Function to calculate the average age of students
def calculate_average_age(students):
  total_age = sum(student['age'] for student in students)
  return total_age / len(students)

# Example usage of the calculate_average_age function
average_age = calculate_average_age(students)
print(f"The average age of students is: {average_age}")  
# Output: The average age of students is: 22.333333333333332

# Function to find a student by name
def find_student_by_name(students, name):
  for student in students:
    if student['name'].lower() == name.lower():
      return student
  return None

# Example usage of the find_student_by_name function
student_name = "Budi"
found_student = find_student_by_name(students, student_name)
if found_student:
  print(f"Found student: {found_student}")  
else:
  print(f"Student {student_name} not found.") 
# Output: Found student: {'name': 'Budi', 'age': 20, 'major': 'Informatics'}

# Function to add a new student
def add_student(students, name, age, major):
  new_student = {"name": name, "age": age, "major": major}
  students.append(new_student)
  print(f"Added new student: {new_student}")

# Example usage of the add_student function
add_student(students, "Dodi", 23, "Physics")
print_student_info(students) 