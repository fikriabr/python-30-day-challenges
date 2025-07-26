# Sample code 1
# Conditional Logic Example
# This code checks the temperature and prints a message based on the condition
temperature = 25

if temperature > 30:
    # Do something if the temperature is above 30
    print("It's a hot day.")
elif temperature < 15:
    # Do something if the temperature is below 15
    print("It's a cold day.")
else:
    # Do something if the temperature is between 15 and 30
    print("It's a pleasant day.")

# Sample code 2
# Conditional Logic with Multiple Conditions
# This code checks if a person can drive based on age and license status
age = 20
have_license = True

if age >= 18 and have_license:
    # Do something if the person is 18 or older and has a license
    print("You can drive.")
else:
    # Do something if the person is under 18 or does not have a license
    print("You cannot drive.")
