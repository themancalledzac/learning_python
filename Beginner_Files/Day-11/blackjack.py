from art import logo
import random
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
your_score = sum(your_cards)
computer_cards = []
computer_score = 0

# ask "do you want to play a game of Blackjack? Type 'y' or 'n': "


def blackjack():
    answer = input(
        "Would you like to play a game of Blackjack? Type 'y' for yes, or 'n' for no: ")
    if answer == "n":
        return
    os.system("cls")
    print(logo)
    initial_cards()
    return_scores()
    deal()


def initial_cards():
    while len(your_cards) < 2:
        next_card = hit_me()
        your_cards.append(next_card)
        global your_score
        your_score = sum(your_cards)
    while len(computer_cards) < 2:
        computer_cards.append(hit_me())
        global computer_score
        computer_score = sum(computer_cards)


def return_scores():
    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")


def deal():
    global your_score
    global your_cards
    global computer_score
    global computer_cards
    answer = deal_again()
    if answer == "y":
        your_cards.append(hit_me())
        your_score = sum(your_cards)
        computer_cards.append(hit_me())
        computer_score = sum(computer_cards)
        if your_score > 21:
            lose()
        else:
            return_scores()
            deal()
    else:
        finish()


def deal_again():
    return input("Type 'y' to get another card, type 'n' to pass: ")


def hit_me():
    return random.choice(cards)


def lose():
    return_scores()
    print("You went over. You lose! ")
    blackjack()


def finish():
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if your_score > computer_score:
        print("You win!")
        blackjack()
    else:
        print("You lose!")
        blackjack()


blackjack()
