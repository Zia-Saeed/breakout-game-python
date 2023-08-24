from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("blue")
        self.initial_position()
        self.x_move = 12
        self.y_move = 12


    def initial_position(self):
        self.penup()
        self.hideturtle()
        self.goto(0, -315)
        self.showturtle()

    def ball_move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def detect_collision_with_right_wall(self):
        self.x_move *= - 1

    def detect_collision_with_left_wall(self):
        self.x_move *= -1

    def detect_collision_with_upper_wall(self):
        self.y_move *= - 1

    def detect_collision_with_handle(self):
        self.y_move *= - 1

    def detect_collision_with_hurdles(self):
        self.y_move *= - 1