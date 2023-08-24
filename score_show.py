from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.score = 0
        self.score_move()

    def score_move(self):
        self.penup()
        self.goto(self.position)
        self.hideturtle()
        self.color("White")
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_move()

