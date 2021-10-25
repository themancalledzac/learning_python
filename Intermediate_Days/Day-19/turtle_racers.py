from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def play_game():
    is_race_on = False
    characters = ["leonardo", "raphael",
                  "donatello", "michelangelo", "zac", "tara"]
    all_turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    difference = 20
    pointer = 0

    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle will win the race? Enter a color: ")
    if user_bet not in colors:
        print("please choose a valid color")
        play_game()

    print(user_bet)

    for new_turtle in characters:
        height = -50
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[0 + pointer])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=height + (difference * len(characters)))
        pointer += 1
        difference -= 5
        new_turtle.pendown()
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(
                        f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(
                        f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


play_game()

screen.exitonclick()
