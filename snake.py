"""
This program contains the snake class that controls all snake related functions.
"""


from turtle import Turtle

SNAKE_ORIGINAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in SNAKE_ORIGINAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_segment = Turtle(shape='square')
        new_snake_segment.penup()
        new_snake_segment.color('white')
        new_snake_segment.goto(position)
        self.snake_segments.append(new_snake_segment)

    def extend_segment(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for snake_segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_segment_num - 1].xcor()
            new_y = self.snake_segments[snake_segment_num - 1].ycor()
            self.snake_segments[snake_segment_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

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
