"""
This program emulates the classic snake game.
"""


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(height=600, width=600)
s.bgcolor('black')
s.title('Snake')
s.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(fun=snake.up, key='Up')
s.onkey(fun=snake.down, key='Down')
s.onkey(fun=snake.left, key='Left')
s.onkey(fun=snake.right, key='Right')

while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.update()
        score.write_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_on = False
        score.game_over()

    # Detect collision with body
    for snake_segment in snake.snake_segments[1:]:
        if snake.head.distance(snake_segment) < 10:
            game_on = False
            score.game_over()

s.exitonclick()
