from datetime import date
# Pyhton data types

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview

# Integer
age = 18

# Float (AKA Floating point number)
current_balance = 51.28

# Boolean
is_tall = False  # can be set to either True or False

# String
message = "Have a nice day"

# List
my_list = ["apples", 5, 7.3]

# Dictionary
my_dictionary = {'amount': 75}

# Tuple
coordinates = (40, 74)  # can NOT be changed later
# tuple example
# ----------------------------------------
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# ----------------------------------------

# Set
my_set = {5, 6, 3}


# math

3 + 5
7 - 5
3 * 4
6 / 3
2 ** 3  # 2 to the power of 3
8 // 3  # floor division
result = 4 / 2
result /= 2  # divide equal, just like javascript
result += 1
result -= 1


# round
# number = round(number) Round the total number
# number = round(number, 2) Round to 2 decimal places


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / (float(height) * float(height))
bmi_round = round(bmi, 2)
bmIndex = "Normal"
if bmi < 18.5:
    bmIndex = "Underweight"
elif bmi >= 18.5 and bmi <= 25:
    bmIndex = "Normal Weight"
elif bmi > 25 and bmi <= 30:
    bmIndex = "Overweight"
elif bmi > 30:
    bmIndex = "Obese"

print(f"Your body mass index is {bmi_round} Which means you are {bmIndex}")

# f-string
# print(f"Your body mass index is {bmi_round} Which means you are {bmIndex}")


# age = input("What is your current age? ")

# today = str(date.today())
# print(today)

# age_int = int(age)

# years_remaining = 90 - age_int
# months_remaining = years_remaining * 12
# weeks_remaining = years_remaining * 52
# days_remaining = years_remaining * 365

# print(f"{months_remaining} months remaining.")
# print(f"{weeks_remaining} weeks remaining.")
# print(f"{days_remaining} days remaining.")


# TIP CALCULATOR

print("Welcome to the tip Calculator.")

total = input("What was the total bill? ")  # 124.56

tip_percent = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")  # 12

how_many_people = input("How many people to split the bill? ")  # 7

total_with_tip = (float(total) * float(tip_percent) * .01) + float(total)

per_person = total_with_tip / int(how_many_people)
per_person_round = round(per_person, 2)

print(f"Each person should pay: {per_person_round}.")
