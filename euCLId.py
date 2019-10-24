import turtle
window = turtle.Screen

#stylistic note: seac stands for Straight Edge And Compass
seac = turtle.Turtle()
seac.ht()
seac.speed(0)
seac.home()
seac.pu()

#define a point, its coordinates are arbitary:
A = (-200,100)
seac.setpos(A)
seac.dot()

#define a point, its coordinates are arbitary:
B = (100, 200)
seac.setpos(B)
seac.dot()

#circle class object under construction as of October 24, 2019
#class euCircle:
#    def __init__():
        


def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards(ptA)-90)
	radius=seac.distance(ptA)
	seac.circle(radius)
	seac.pu()
	
circthru(A,B)
circthru(B,A)
turtle.exitonclick()
