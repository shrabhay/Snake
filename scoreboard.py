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
        with open(file='high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score} HIGH SCORE: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GAME OVER!', move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.write_score()
