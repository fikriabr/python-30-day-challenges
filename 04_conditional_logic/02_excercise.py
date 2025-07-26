score = int(input("Enter your score: "))

grade = ""

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
elif score >= 0 and score < 60:
    grade = "F"
else:
    grade = "Invalid score"

if grade == "Invalid score":
    print("Please enter a valid score between 0 and 100.")
else:
  print(f"Your grade is: {grade}")