from turtle import Turtle

# In PYTHON, a const, or constant variable is in all caps
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
segments = []
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # self.length = length
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for square in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square - 1].xcor()
            new_y = self.segments[square - 1].ycor()
            self.segments[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        if self.head

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
