# degugging

# describe problem
from random import randint


# def my_function():
#     for i in range(1, 20):
#         # Range is basically up to 20, but not including 20
#         if i == 20:
#             print("You got it")


# my_function()

# reproduce the bug

dice_nums = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_num)
print(dice_nums[dice_num])
