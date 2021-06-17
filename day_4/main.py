from turtle import Turtle, Screen

tur = Turtle()
tur.shape("arrow")
tur.color("black")

for _ in range(50):
	if tur.isdown():
		tur.penup()
	else:
		tur.pendown()
	tur.forward(10)

scrn = Screen()
scrn.exitonclick()
