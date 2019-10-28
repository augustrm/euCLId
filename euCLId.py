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
		self.shape = 'point'
	def __iter__(self):
		yield(self.xy)
	def __getitem__(self, i):
		return self.xy[i]
	def __str__(self):
		return self.name



class euCircle:
	def __init__(self, center_point, radial_point, name, n=1000):
		self.name = name
		self.shape = 'circle'
		self.c = center_point
		self.r_p = radial_point
		self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)
		#coordinate container list:
		self.xy = []
		#populate coordinate container list:
		for i in range(0, n+1):
			self.xy.append((self.c[0] + cos(2*pi/n*i)*self.radius, self.c[1] + sin(2*pi/n*i)*self.radius))

position_data = {}

def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards((ptA[0],ptA[1]))-90)
	#make the newly generated euCircle globally accessible as a variable:
	globals()["circ"+str(ptA)+str(ptB)] = euCircle((ptA[0], ptA[1]), (ptB[0], ptB[1]),"circ"+str(ptA)+str(ptB))
	radius = seac.distance((ptA[0],ptA[1]))
	seac.circle(radius)
	seac.pu()


def intersect(obj1, obj2):
	if obj1.shape == 'circle' and obj2.shape == 'circle':
		distance = sqrt((obj2.c[0] - obj1.c[0])**2 + (obj2.c[1] - obj1.c[1])**2)
		#case of non intersecting circles:
		if distance > obj1.radius + obj2.radius:
			return None
		#case of one circle residing wholly within another:
		elif distance < abs(obj1.radius - obj2.radius):
			return None
		#case of circles coinciding, and therefore being equal:
		elif distance == 0 and obj1.radius == obj2.radius:
			return None
		else:
			a = (obj1.radius**2 - obj2.radius**2 + distance**2) / (2 * distance)
			h = sqrt(obj1.radius**2 - a**2)
			x2 = obj1.c[0] + a * (obj2.c[0] - obj1.c[0]) / distance
			y2 = obj1.c[1] + a * (obj2.c[1] - obj1.c[1]) / distance
			x3 = x2 + h * (obj2.c[1] - obj1.c[1]) / distance  
			y3 = y2 - h * (obj2.c[0] - obj1.c[0]) / distance
			x4 = x2 - h * (obj2.c[1] - obj1.c[1]) / distance  
			y4 = y2 + h * (obj2.c[0] - obj1.c[0]) / distance
			#add intersect points to globals; in form of "circAB_intersect_circBA_1"
			globals()[obj1.name+"_intersect_"+obj2.name+"_1"] = euPoint(x3, y3, obj1.name+"_intersect_"+obj2.name+"_1")
			globals()[obj1.name+"_intersect_"+obj2.name+"_2"] = euPoint(x4, y4, obj1.name+"_intersect_"+obj2.name+"_1")
			#draw intersect 1:
			seac.pu()
			seac.setpos(x3,y3)
			seac.pd()
			seac.dot()
			seac.pu()
			#draw intersect 2:
			seac.pu()
			seac.setpos(x4,y4)
			seac.pd()
			seac.dot()
			seac.pu()
			#send seac to origin (0,0)
			seac.home
			return [(x3,y3), (x4,y4)]

			
			#testing:
#define a point, its coordinates are arbitary:
A = euPoint(200,200, "A")
seac.setpos(A.xy)
seac.dot()

#define a point, its coordinates are arbitary:
B = euPoint(-100, -500, "B")
seac.setpos(B.xy)
seac.dot()

seac.color("blue")


circthru(A,B)
circthru(B,A)
print(intersect(circAB, circBA))
#
#print(circAB.xy)
turtle.exitonclick()
