import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input(
    "What do you choose? Type 0 for Rock, 1, for Paper or 2 for Scissors. ")
choice_int = int(choice)

computer_choice = random.randint(0, 2)

if choice_int == 1:
    if computer_choice == 1:
        print(
            f"you Choose rock:\n{rock}\nand computer chooses rock:\n{rock}\nIt's a tie!")
    elif computer_choice == 2:
        print(
            f"you Choose rock:\n{rock}\nand computer chooses paper:\n{paper}\nYou Lose!")
    elif computer_choice == 3:
        print(
            f"you Choose rock:\n{rock}\nand computer chooses scissors:\n{scissors}\nYou Win!")
if choice_int == 2:
    if computer_choice == 1:
        print(
            f"you Choose paper:\n{paper}\nand computer chooses rock:\n{rock}\nYou win!")
    elif computer_choice == 2:
        print(
            f"you Choose paper:\n{paper}\nand computer chooses paper:\n{paper}\nYou tie!")
    elif computer_choice == 3:
        print(
            f"you Choose paper:\n{paper}\nand computer chooses scissors:\n{scissors}\nYou Lose!")
if choice_int == 3:
    if computer_choice == 1:
        print(
            f"you Choose scissors:\n{scissors}\nand computer chooses rock:\n{rock}\nYou Lose!")
    elif computer_choice == 2:
        print(
            f"you Choose scissors:\n{scissors}\nand computer chooses paper:\n{paper}\nYou Win!")
    elif computer_choice == 3:
        print(
            f"you Choose scissors:\n{scissors}\nand computer chooses scissors:\n{scissors}\nYou Tie!")
