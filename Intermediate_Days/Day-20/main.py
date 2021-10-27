from turtle import Screen, Turtle
from pprint import pprint

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

length = 3
snake = []


def initial_snake():
    for square_index in range(0, length):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        current_x = 0
        if square_index == 0:
            new_turtle.goto(x=0, y=0)
            current_x = 0
        else:
            new_turtle.goto(x=(-20 * (square_index)), y=0)
            current_x = float(-20 * (square_index - 1))
            future_position = (current_x, 0.00)
            new_turtle.future_position = tuple(future_position)
            print(new_turtle.future_position)
            print(new_turtle.position())

        snake.append(new_turtle)
    # print(snake[0])
    move()


def move():
    # check if position matches any other position in snake, if so, exit
    print("let's move")
    #

    # setattr(_obj=initial_snake,
    #         _name="future_position", _value=(new_turtle.position()))

    # pprint(dir(new_turtle))
    # print(new_turtle.future_position)
    # pprint(vars(new_turtle))

# our new_turtle's attribute: position gives us the exact position.add()
# on move, we need to move through every object that is appended to 'snake'
# on move,


# create initial square. square 1.
# add square to list of squares
# for each square in list, they follow the next in list
# for each square, a location is given, and a future location. on change, we
initial_snake()
screen.exitonclick()
