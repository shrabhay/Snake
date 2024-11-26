"""
This program contains the Scoreboard class that controls everything related to the player score.
"""


from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER!', move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
