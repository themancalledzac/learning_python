from art import higher_or_lower_logo as logo
from art import vs
from random import randint
from game_data import data
import os

person_a = data[randint(0, 49)]
person_b = data[randint(0, 49)]
score = 0

print(logo)


def start():
    compare(person_a)
    print(vs)
    compare(person_b)
    guess()


def compare(person):
    if person == person_a:
        print(f"Compare A: {person['name']}, a {person['description']}. ")
    elif person == person_b:
        print(f"Against B: {person['name']} a {person['description']}. ")


def guess():
    global person_a
    p_a_count = person_a["follower_count"]
    p_b_count = person_b["follower_count"]
    # global person_b
    player_guess = input("Who has more followers? Type 'A' or 'B': ")
    if player_guess == "A" or player_guess == "a":
        if p_a_count > p_b_count:
            win()
        else:
            lose()
    elif player_guess == "B" or player_guess == "b":
        if p_a_count < p_b_count:
            win()
        else:
            lose()
    else:
        return print("Please, from now on, could you follow the directions and type 'A' or 'B'? Dang. ")


def win():
    global score
    score += 1
    os.system("cls")
    print(logo)
    print(f"You're right! Current score: {score}. ")
    randomize()
    start()


def lose():
    global score
    print(f"Sorry, that's wrong. Final score: {score}")
    return


def randomize():
    global person_a
    global person_b
    person_a = person_b
    person_b = data[randint(0, 49)]


start()
