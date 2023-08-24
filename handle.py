from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.color("white")
        self.initial_position()

    def initial_position(self):
        self.penup()
        self.hideturtle()
        self.goto(10, -335)
        self.showturtle()

    def move_right(self):
        new_x = self.xcor() + 35
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 35
        self.goto(new_x, self.ycor())

