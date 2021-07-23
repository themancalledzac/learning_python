# 3-1-exercise

# number = int(input("Which number do you want to check? "))

# if number % 2:
#     print("odd")
# else:
#     print("even")


# or... apparently this is the correct way

# if number % 2 == 0:
#     print("even")
# else:
#     print("This is an odd number.")


# height = int(input("What is your height? "))

# if height > 120:
#     age = int(input("What is your age? "))
#     if age > 18:
#         print("It is $12 to ride this ride punk.")
#     elif age >= 12 & age <= 18:
#         print("It's 7 bucks youngin")
#     else:
#         print("It is $5 to ride this ride youngin")
# else:
#     print("sorry to short, shorrty.")


# LEAP YEAR TASK
# -------------------------------------------------------------------------------

# year = int(input("which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This year is a leap year.")
#         else:
#             print("this year is not a leap year")
#     else:
#         print("This year is a leap year")
# else:
#     print("it is not a leap year")


# rollarcoaster round two
# -------------------------------------------------------------------------------

# height = int(input("What is your height? "))
# total = 0

# if height > 120:
#     age = int(input("What is your age? "))
#     if age < 12:
#         total += 5
#         print("child tickets are $5.")
#     if age <= 18 & age >= 12:
#         total += 7
#         print("Youth tickets are $7.")
#     if age > 18:
#         total += 12
#         print("Adult tickets are $12.")

#     photos = (input("do you want photos? Y or N. "))
#     if photos == "Y":
#         total += 3

#     print(f"the total bill is {total}")


# else:
#     print("TOO SHORT BUCKO")

# pizza Order
# -------------------------------------------------------------------------------

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# if size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1

# if size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     print("can you type the correct thing you stupid shit")

# print(f"Your final bill will be ${bill}.")

# -------------------------------------------------------------------------------

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1Lower = name1.lower()
name2Lower = name2.lower()
true = "true"
love = "love"
trueCount = 0
loveCount = 0

name1Count = name1.count('love')
# for loop, for every letter in 'love', do a count += 1
for x in true:
    trueCount += name1Lower.count(x)
    trueCount += name2Lower.count(x)

for y in love:
    loveCount += name1Lower.count(y)
    loveCount += name2Lower.count(y)


loveString = str(loveCount)
trueString = str(trueCount)

loveScore = int(loveString + trueString)

if loveScore < 10 and loveScore > 90:
    print(
        f"Your score is {loveScore} and you go together like coke and mentos")
if loveScore < 50 and loveScore > 40:
    print(f"Your score is {loveScore} and you are alright together.")
else:
    print(f"Your score is {loveScore}")
