# for number in range(1, 11, 3):
#     print(number)
#     # this gives us between 1 and 11, includeing 1, but not including 11, and increment by 3
#     #which results in 1, 4, 7, 10


# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# Adding Evens
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 + 10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
