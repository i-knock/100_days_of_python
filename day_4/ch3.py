from turtle import Turtle, Screen
import random
random.seed()

tur = Turtle()
tur.shape("arrow")
tur.color("black")

shapes = [sides for sides in range(3, 10)]

for sides in shapes:
    color = [random.randrange(1, 100, 1)/100 for _ in range(3)]
    for _ in range(sides):
        tur.forward(100)
        tur.rt(360/sides)
        tur.color(color)


scrn = Screen()
scrn.exitonclick()
