example_dictionary = {
    "Bug": "An error in a program.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retreiving items from dictionary
print(example_dictionary["Function"])

# Adding new items to dictionary.
example_dictionary["Loop"] = "The action of doing something over and over again."
print(example_dictionary)


# Create an empty dictionary
empty_dictionary = {}


# wipe an existing dictionary
# example_dictionary = {}
# print(example_dictionary)

# Edit an item in a dictionary
example_dictionary["Bug"] = "A new definition by editing it"

print(example_dictionary)

# Loop through a dictionary
for key in example_dictionary:
    print(key)
    print(example_dictionary[key])
