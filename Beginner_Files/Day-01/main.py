# Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

# 1-2-exercise
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print("hello" + " " + "world")


# 1-2-exercise
# fix code below

print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print("e.g. print('Hello'" + " " + "'world')")
print(("New lines can be created with a backslash and n."))


print("Hello " + input("What is your name?"))

# 1-3-exercise

print(len(input("what is your name? ")))

# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Python variables

name = input("What is your station? ")

print(name)

# 1-4-exercise

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
shortterm = a
a = b
b = shortterm

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# Band Name Generator

print("welcome to the Band Name Generator\nFirst question is: ")
pet_name = input("what is the name of your first pet? ")
city_name = input("What is the city you grew up in? ")
print("Thank you!\nCalculating your band name now...\nLooks like your band name is '" +
      city_name + " " + pet_name + "'!\nHope you enjoyed")
