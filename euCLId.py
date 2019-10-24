import turtle
window = turtle.Screen
seac = turtle.Turtle()
#stylistic note: seac stands for Straight Edge And Compass
seac.ht()
turtle.tracer()
seac.home()
seac.pu()

A = (-200,100)
seac.setpos(A)
seac.dot()

B = (100, 200)
seac.setpos(B)
seac.dot()

def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards(ptA)-90)
	radius=seac.distance(ptA)
	seac.circle(radius)
	seac.pu()
	
circthru(A,B)
circthru(B,A)
