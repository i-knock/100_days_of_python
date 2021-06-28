'''
Spirograph
- Radius of a 100
- Random colors
- Change tilt of circle
'''

from turtle import Turtle, Screen
import random
random.seed()

tur = Turtle()
scrn = Screen()
scrn.colormode(255)

tur.speed('fastest')

prev_angle = -1
while prev_angle < tur.heading():
    color = tuple([random.randint(1, 255) for _ in range(3)])
    tur.pencolor(color)
    tur.circle(100)
    prev_angle = tur.heading()
    tur.left(10)

scrn.exitonclick()