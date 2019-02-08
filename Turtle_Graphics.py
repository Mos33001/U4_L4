from turtle import *


mos = Turtle()

mos.color("turquoise")
mos.pensize(5)
mos.speed(2)
mos.turtlesize(2,2,2)
mos.shape("turtle")



for x in range(4):
	mos.forward(80)
	mos.left(50)
	mos.forward(200)
	mos.right(150)
	mos.forward(50)
	mos.circle(25)
	mos.backward(30)
	mos.circle(50)



mainloop()