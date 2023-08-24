from ball import Ball
from turtle import Screen
from handle import Paddle
from hurdle_obj import Hurdles
import time
from score_show import Score
from turtle import Turtle
from highest_score import HighestScore


ALIGNMENT = 'center'
FONT = ("Courier", 40, "normal")
SLEEP_TIME = 0.1

if __name__ == '__main__':


    # with open("score.txt", "w") as file:
    #     file.write("1")

    screen = Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("black")
    screen.title("Welcome to Breakout game.")

    screen.tracer(0)

    ball = Ball()
    paddle = Paddle()
    hurdles = Hurdles()
    score = Score(position=(0, 330))

    screen.listen()

    screen.onkey(key="d", fun=paddle.move_right)
    screen.onkey(key="a", fun=paddle.move_left)
    high_score = HighestScore()

    while True:
        screen.update()
        ball.ball_move()
        time.sleep(SLEEP_TIME)

        if ball.xcor() > 380:
            ball.detect_collision_with_right_wall()

        elif ball.xcor() < -380:
            ball.detect_collision_with_left_wall()

        elif ball.ycor() > 340:
            ball.detect_collision_with_upper_wall()

        elif ball.distance(paddle) < 32:
            ball.detect_collision_with_handle()

        elif ball.ycor() < - 360:
            new_x, new_y = (paddle.xcor(), paddle.ycor())
            ball.goto(new_x, new_y + 20)

        elif len(hurdles.obj) <= 0:
            result = Turtle()
            result.penup()
            result.goto(0, 0)
            result.write(f"You Win!", align=ALIGNMENT, font=FONT)

        else:
            for ob in hurdles.obj:
                if ball.distance(ob) < 10:
                    ob.hideturtle()
                    hurdles.obj.remove(ob)
                    ball.detect_collision_with_hurdles()
                    score.increase_score()
                    SLEEP_TIME = 0.03

        with open("score.txt", "r") as file:
            higest_score = file.readline()
            if int(higest_score) < score.score:
                with open("score.txt", "w") as file:
                    file.write(str(score.score))

    screen.exitonclick()

