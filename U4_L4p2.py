from turtle import *


mos = Turtle()

mos.color("turquoise")
mos.pensize(5)
mos.speed(2)
mos.turtlesize(2,2,2)
mos.shape("turtle")



for x in range(4):
	mos.forward(180)
	mos.left(90)



mainloop()