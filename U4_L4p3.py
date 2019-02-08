from turtle import *


mos = Turtle()

mos.color("turquoise")
mos.pensize(5)
mos.speed(2)
mos.turtlesize(2,2,2)
mos.shape("turtle")



for x in range(6):
	mos.forward(80)
	mos.left(60)



mainloop()