from turtle import Turtle, Screen
import random
random.seed()

tur = Turtle()
tur.shape("arrow")
tur.color("black")
tur.pensize(15)
tur.speed('fastest')

scrn = Screen()
scrn.colormode(255)

# DONE: Random walk
'''
1) Goes up/down/left/right randomly
2) Thicker line
3) Faster movement.
4) Random color
'''

iterations = 500
angles = [90*i for i in range(4)]

for it in range(iterations):
    color = tuple([random.randrange(1, 255, 1) for _ in range(3)])
    angle = random.choice(angles)
    tur.pencolor(color)
    tur.right(angle)
    tur.forward(20)

scrn.exitonclick()
