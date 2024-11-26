"""
This program emulates the classic snake game.
"""


from turtle import Screen
from snake import Snake
import time

s = Screen()
s.setup(height=600, width=600)
s.bgcolor('black')
s.title('Snake')
s.tracer(0)

snake = Snake()
game_on = True

s.listen()
s.onkey(fun=snake.up, key='Up')
s.onkey(fun=snake.down, key='Down')
s.onkey(fun=snake.left, key='Left')
s.onkey(fun=snake.right, key='Right')

while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

s.exitonclick()
