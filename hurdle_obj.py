from turtle import Turtle
import random


class Hurdles(Turtle):
    def __init__(self):
        super().__init__()
        self.create_hurdle()

    def create_hurdle(self):
        self.obj = []
        y = 300
        color_list = [
            "aliceblue",
            "antiquewhite",
            "aqua",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "black",
            "blanchedalmond",
            "blue",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "fuchsia",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "gray",
            "green",
            "greenyellow",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",]
        x_pos = [-390, -380, -370, -360, -350, -340, -330, -320]
        loop_run = 45
        for i in range(8):
            for obj in range(loop_run):
                obj = Turtle()
                obj.shape("square")
                obj.color(random.choice(color_list))
                obj.shapesize(stretch_wid=0.3, stretch_len=0.5)
                obj.penup()
                obj.goto(x_pos[i], y)
                rand_num = random.randint(15, 20)
                x_pos[i] += rand_num
                self.obj.append(obj)
            y -= 20
            loop_run -= 2
