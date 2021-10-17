# Part 1

# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")


# for _ in range(4):
#     timmy_the_turtle.forward(250)
#     timmy_the_turtle.right(90)


import turtle as t
import heroes

print(heroes.gen())

tim = t.Turtle()
screeny = t.Screen()

# part 2
# tim.shape("turtle")
# tim.color("blue")


# def draw_line():
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# def move():
#     for _ in range(10):
#         draw_line()


# move()


def move():
    number_of_sides = 3
    angle = 360 / number_of_sides
    color_number = "#000000"
    print(color_number)
    print(type(color_number))
    tim.pencolor("#285078")
    for _ in range(8):
        tim.color(color_number)
        for _ in range(number_of_sides):
            print(number_of_sides)
            print(angle)
            draw_line()
            tim.right(angle)
        number_of_sides += 1
        angle = 360 / number_of_sides
        color_number = color_number[1:]
        print(color_number)
        print(type(color_number))
        color_number = int(color_number)
        color_number += 111111
        color_number = f"#{color_number}"
        print("here lies our color_number")
        print(type(color_number))
        print(color_number)


def draw_line():
    tim.forward(20)


move()


screeny.exitonclick()
