'''
Hirst Painting (i.e. dots)
'''

import colorgram
from turtle import Turtle, Screen
from random import seed, choice
seed()

tur = Turtle()
scrn = Screen()
scrn.colormode(255)

# Extract colors from image and obtain rgb list
colors = colorgram.extract('day_4/hirst_painting.png', 16)
colors = [tuple([color.rgb[i] for i in range(3)]) for color in colors]
colors = [color for color in colors if all(elem<=230 for elem in color)] # remove white

# Drawing the dots
num_dots_line = 10
tur.penup()
tur.hideturtle()
tur.speed('fastest')
offset = 250
for i in range(num_dots_line):
    tur.setpos(0-offset, i*50-offset)
    for _ in  range(num_dots_line):
        tur.dot(20, choice(colors))
        tur.forward(50)

scrn.exitonclick()
print(colors)