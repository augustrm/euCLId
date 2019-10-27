import turtle
from math import cos, sin, sqrt, pi
window = turtle.Screen

#stylistic note: seac stands for Straight Edge And Compass
seac = turtle.Turtle()
seac.ht()
seac.speed(0)
seac.home()
seac.pu()
seac.color("red")

class euPoint:
	def __init__(self, x, y, name):
		self.coords = (x,y)
		self.name = name
	def __iter__(self):
		return((self.x, self.y))


#define a point, its coordinates are arbitary:
A = euPoint(0,23, "A")
seac.setpos(A.coords)
seac.dot()

#define a point, its coordinates are arbitary:
B = euPoint(200, 200, "B")
seac.setpos(B.coords)
seac.dot()

seac.color("blue")


class euCircle:
	def __init__(self, center_point, radial_point, name, n=1000):
		self.name = name
		self.c = center_point
		self.r_p = radial_point
		self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)
		self.circ_coords = []
		for i in range(0, n+1):
			self.circ_coords.append((self.c[0] + cos(2*pi/n*i)*self.radius, self.c[1] + sin(2*pi/n*i)*self.radius))


def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards((ptA[0],ptA[1]))-90)
	radius=seac.distance(ptA)
	seac.circle(radius)
	seac.pu()

circthru(A,B)
#circthru(B.coords,A.coords)
turtle.exitonclick()
