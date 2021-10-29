from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

length = 3
game_is_on = True
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
    start_game()


def turn_left(this):
    this.left(90)


def turn_right(this):
    this.right(90)


def start_game():
    screen.update()
    # check if position matches any other position in snake, if so, exit

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        # range(start, stop, step)
        for square in range(len(snake) - 1, 0, -1):
            new_x = snake[square - 1].xcor()
            new_y = snake[square - 1].ycor()
            snake[square].goto(new_x, new_y)

        snake[0].forward(20)
        snake[0].forward(20)
        snake[0].left(90)


    #


screen.listen()
initial_snake()
screen.exitonclick()
