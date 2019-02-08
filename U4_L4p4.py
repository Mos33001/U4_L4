from turtle import *


mos = Turtle()
kal = Turtle() 

mos.color("turquoise")
mos.pensize(5)
mos.speed(2)
mos.turtlesize(2,2,2)
mos.shape("turtle")

kal.color("red")
kal.pensize(5)
kal.speed(2)
kal.turtlesize(2,2,2)
kal.shape("turtle")



for x in range(3):
	mos.forward(80)
	mos.left(120)
	kal.circle(50)

mainloop()