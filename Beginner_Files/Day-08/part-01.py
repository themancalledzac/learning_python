# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet(parameter):
#     print(f"Welcome to the store, {parameter}")
#     print("hello")
#     print("ok?")


# argument = "zac"
# greet(argument)

# Functions with more than 1 input

def greet_with(name, location):
    print(f"Welcome to {location}, {name}")


name_argument = "Zac"
location_argument = "London"
greet_with(name_argument, location_argument)
