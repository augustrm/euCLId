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
		self.xy = (x,y)
		self.name = name
	def __iter__(self):
		yield(self.xy)
	def __getitem__(self, i):
		return self.xy[i]
	def __str__(self):
		return self.name


#define a point, its coordinates are arbitary:
A = euPoint(0,23, "A")
seac.setpos(A.xy)
seac.dot()

#define a point, its coordinates are arbitary:
B = euPoint(200, 200, "B")
seac.setpos(B.xy)
seac.dot()

seac.color("blue")


class euCircle:
	def __init__(self, center_point, radial_point, name, n=1000):
		self.name = name
		self.c = center_point
		self.r_p = radial_point
		self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)
		self.circ_xy = []
		for i in range(0, n+1):
			self.circ_xy.append((self.c[0] + cos(2*pi/n*i)*self.radius, self.c[1] + sin(2*pi/n*i)*self.radius))

circ_data = {}

def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards((ptA[0],ptA[1]))-90)
	circ_data["circ"+str(ptA)+str(ptB)] = euCircle((ptA[1], ptA[0]), (ptB[0], ptB[1]),"circ"+str(ptA)+str(ptB))
	radius = seac.distance((ptA[0],ptA[1]))
	seac.circle(radius)
	seac.pu()


circthru(A,B)
print(circ_data["circAB"].circ_xy)
#circthru(B.xy,A.xy)
turtle.exitonclick()
