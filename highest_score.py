from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")


class HighestScore(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score()

    def highest_score(self):
        with open("score.txt", "r") as file:
            highest_score = int(file.read())
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(-280, 330)
        self.color("White")
        self.write(f"Highest Score = {highest_score}", align=ALIGNMENT, font=FONT)