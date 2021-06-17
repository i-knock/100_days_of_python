# TODO: Draw any shape formed by straight lines (i.e. squares, triangles, etc).
from turtle import Turtle, Screen
import random
random.seed()

tur = Turtle()
tur.shape("arrow")
tur.color("black")

shapes = [sides for sides in range(3, 10)]


for sides in shapes:
    for _ in range(sides):
        tur.forward(100)
        tur.rt(360/sides)
        color = [float(random.randrange(1, 255, 1)) for _ in range(3)]
        tur.colormode(255)
        tur.pencolor(color)


scrn = Screen()
scrn.exitonclick()
