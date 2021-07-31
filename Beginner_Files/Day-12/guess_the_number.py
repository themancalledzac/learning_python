from art import logo
import random
import os

Number = random.randint(1, 100)
guesses = 0


def play_the_game():
    global guesses
    os.system("cls")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"Psssst, the correct answer is {49}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5
    else:
        print("You idiot, choose easy or hard.")
        return
    attempt()


def attempt():
    global guesses
    global Number
    print(f"You have {guesses} attempts remaining to guess the number.")
    attempt = input("Make a guess: ")
    try:
        attempt = int(attempt)
        attempting(attempt)
    except ValueError:
        print("Not a number")
        return


def attempting(n):
    global Number
    global guesses
    if n < Number:
        wrong("low")
        guesses -= 1
        attempt()
    elif n > Number:
        wrong("high")
        guesses -= 1
        attempt()
    elif n == Number:
        print(f"You got it! The answer was {Number}")
        return


def wrong(n):
    global guesses
    if n == "low":
        print("Too low.")
    elif n == "high":
        print("Too high.")
    if guesses == 1:
        print("You've run out of guesses, you lose.")
        return
    else:
        print("Guess Again.")


play_the_game()
