import turtle
from math import cos, sin, sqrt, pi

turtle.Screen()
turtle.delay(0)
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

		
class euLine:
	def __init__(self, ptA, ptB, name):
		self.name = name
		self.shape = 'line'
		self.ptA = (ptA[0], ptA[1])
		self.ptB = (ptB[0], ptB[1])
		self.slope = (self.ptB[1] - self.ptA[1]) / (self.ptB[0] - self.ptA[0])
	def __str__(self):
		return self.name
		

class euCircle:
	def __init__(self, center_point, radial_point, name, n=1000):
		self.name = name
		self.shape = 'circle'
		self.c = (center_point[0],center_point[1]) 
		self.r_p = (radial_point[0], radial_point[1])
		self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)
		#coordinate container list:
		##self.xy = []
		#populate coordinate container list:
		##for i in range(0, n+1):
		##	self.xy.append((self.c[0] + cos(2*pi/n*i)*self.radius, self.c[1] + sin(2*pi/n*i)*self.radius))
	def __str__(self):
		return self.name
			
########################################################################################################
#                                     end of basic object definitions                                  #
########################################################################################################
def draw_line(ptA, ptB, name=None, show=True):
	if show == True:
		if name == None:
			globals()["line"+str(ptA)+str(ptB)] = euLine(ptA, ptB, "line"+str(ptA)+str(ptB))
		else:
			name=str(name)
			globals()[name] = euLine(ptA, ptB, name)
		seac.pu()
		seac.setpos(ptA[0], ptA[1])
		seac.pd()
		seac.setpos(ptB[0], ptB[1])
		seac.pu()
	else:
		globals()["line"+str(ptA)+str(ptB)] = euLine(ptA, ptB, "line"+str(ptA)+str(ptB))

		
def draw_circle(ptA, ptB, name=None, show=True):
	if show == True:
		#make the newly generated euCircle globally accessible as a variable:
		if name == None:
			globals()["circ"+str(ptA)+str(ptB)] = euCircle((ptA[0], ptA[1]), (ptB[0], ptB[1]),"circ"+str(ptA)+str(ptB))
		else:
			name=str(name)
			globals()[name] = euCircle((ptA[0], ptA[1]), (ptB[0], ptB[1]), name)
		#draw the circle:
		seac.pu()
		seac.setpos(ptB[0], ptB[1])
		seac.setheading(seac.towards((ptA[0],ptA[1]))-90)
		radius = seac.distance((ptA[0],ptA[1]))
		seac.pd()
		seac.circle(radius)
		seac.pu()
		
	else:
		if name == None:
			globals()["circ"+str(ptA)+str(ptB)] = euCircle((ptA[0], ptA[1]), (ptB[0], ptB[1]),"circ"+str(ptA)+str(ptB))
		else:
			name=str(name)
			globals()[name] = euCircle((ptA[0], ptA[1]), (ptB[0], ptB[1]), name)
			
			
def intersect(obj1, obj2, name1=None, name2=None, show=True, show1=True, show2=True):
	# simple 2x2 determinant:
	def _2x2det(a,b,c,d):
		return (a*d)-(c*b)
	
	# modified signum function for circle-line intersect clause:
	def _signum(x):
		if x < 0:
			return (-1)
		else:
			return 1

	# intersect of a singular point and another object is nonsensical, as a point is that which contains no part
	if obj1.shape == 'point' or obj2.shape == 'point':
		pass
	
	# Intersect of a circle and a circle
	# http://mathworld.wolfram.com/Circle-CircleIntersection.html
	elif obj1.shape == 'circle' and obj2.shape == 'circle':
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
			
			# add intersect points to globals; in form of "circAB_intersect_circBA_1" if namestrings are left unset:
			# otherwise the created points are named whatever namestring is supplied.
			if name1 == None:
				globals()[obj1.name+"_intersect_"+obj2.name+"_1"] = euPoint(x3, y3, obj1.name+"_intersect_"+obj2.name+"_1")
			else:
				name1=str(name1) #sanitize name1 so it is always a string
				globals()[name1] = euPoint(x3, y3, name1)
			
			if name2 == None:
				globals()[obj1.name+"_intersect_"+obj2.name+"_2"] = euPoint(x4, y4, obj1.name+"_intersect_"+obj2.name+"_2")
			else:
				name2=str(name2) #sanitize name2 so it is always a string
				globals()[name2] = euPoint(x4, y4, name2)
			
			if show == True:
				if show1 == True:
					#draw intersect 1:
					seac.pu()
					seac.setpos(x3,y3)
					seac.pd()
					seac.dot()
					seac.pu()
					
				if show2 == True:
					#draw intersect 2:
					seac.pu()
					seac.setpos(x4,y4)
					seac.pd()
					seac.dot()
					seac.pu()
			#send seac to origin (0,0)
			seac.home
			return [(x3,y3), (x4,y4)]
	
	# Intersect of a line and a circle or a circle and a line:
	#http://mathworld.wolfram.com/Circle-LineIntersection.html
	elif obj1.shape == 'line' and obj2.shape == 'circle':
		r = obj2.radius
		# adjust coordinates so circle is centered at origin for calculation:
		x_delta , y_delta = -obj2.c[0], -obj2.c[1]
		x1 ,y1 = obj1.ptA[0] + x_delta , obj1.ptA[1] + y_delta
		x2 ,y2 = obj1.ptB[0] + x_delta , obj1.ptB[1] + y_delta
		d_x = x2 - x1
		d_y = y2 - y1
		d_r = sqrt(d_x**2 + d_y**2)
		D = _2x2det(x1, x2, y1, y2)
		x_int1 = ((D * d_y + _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
		y_int1 = ((-D * d_x + abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
		x_int2 = ((D * d_y - _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
		y_int2 = ((-D * d_x - abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
		
		# add intersect points to globals; in form of "circAB_intersect_circBA_1" if namestrings are left unset:
		# otherwise the created points are named whatever namestring is supplied.
		if name1 == None:
			globals()[obj1.name+"_intersect_"+obj2.name+"_1"] = euPoint(x_int1, y_int1, obj1.name+"_intersect_"+obj2.name+"_1")
		else:
			name1=str(name1) #sanitize name1 so it is always a string
			globals()[name1] = euPoint(x_int1, y_int1, name1)
		
		if name2 == None:
			globals()[obj1.name+"_intersect_"+obj2.name+"_2"] = euPoint(x_int2, y_int2, obj1.name+"_intersect_"+obj2.name+"_2")
		else:
			name2=str(name2) #sanitize name2 so it is always a string
			globals()[name2] = euPoint(x_int2, y_int2, name2)
			
		if show == True:
			if show1 == True:
				seac.pu()
				seac.setpos(x_int1,y_int1)
				seac.dot()
				seac.home()
			if show2 == True:
				seac.pu()
				seac.setpos(x_int2,y_int2)
				seac.dot()
				seac.home()
	elif obj1.shape == 'circle' and obj2.shape == 'line':
		r = obj1.radius
		# adjust coordinates so circle is centered at origin for calculation:
		x_delta , y_delta = -obj1.c[0], -obj1.c[1]
		x1 ,y1 = obj2.ptA[0] + x_delta , obj2.ptA[1] + y_delta
		x2 ,y2 = obj2.ptB[0] + x_delta , obj2.ptB[1] + y_delta
		d_x = x2 - x1
		d_y = y2 - y1
		d_r = sqrt(d_x**2 + d_y**2)
		D = _2x2det(x1, x2, y1, y2)
		x_int1 = ((D * d_y + _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
		y_int1 = ((-D * d_x + abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
		x_int2 = ((D * d_y - _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
		y_int2 = ((-D * d_x - abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
		
		# add intersect points to globals; in form of "circAB_intersect_circBA_1" if namestrings are left unset:
		# otherwise the created points are named whatever namestring is supplied.
		if name1 == None:
			globals()[obj1.name+"_intersect_"+obj2.name+"_1"] = euPoint(x_int1, y_int1, obj1.name+"_intersect_"+obj2.name+"_1")
		else:
			name1=str(name1) #sanitize name1 so it is always a string
			globals()[name1] = euPoint(x_int1, y_int1, name1)
		
		if name2 == None:
			globals()[obj1.name+"_intersect_"+obj2.name+"_2"] = euPoint(x_int2, y_int2, obj1.name+"_intersect_"+obj2.name+"_2")
		else:
			name2=str(name2) #sanitize name2 so it is always a string
			globals()[name2] = euPoint(x_int2, y_int2, name2)
			
		if show == True:
			if show1 == True:
				seac.pu()
				seac.setpos(x_int1,y_int1)
				seac.dot()
				seac.home()
			if show2 == True:
				seac.pu()
				seac.setpos(x_int2,y_int2)
				seac.dot()
				seac.home()

#testing:
#define a point, its coordinates are arbitrary:
A = euPoint(100,50, "A")
seac.setpos(A.xy)
seac.dot()

#define a point, its coordinates are arbitrary:
B = euPoint(20, -39, "B")
seac.setpos(B.xy)
seac.dot()

C = euPoint(80, 130, "C")
seac.setpos(C.xy)
seac.dot()

seac.color("blue")


draw_circle(A,B, show=False)
draw_circle(B,A, show=False)
draw_line(A,B)
intersect(circAB, circBA, name1='E',show2=False)
draw_line(E,A)
draw_line(E,B)
seac.color("green")
draw_circle(C,B)
draw_circle(C,A)
draw_circle(C,E)
intersect(circCE, lineAB, name1 ='beta', show1=False)
intersect(lineEA, circCA, name1='delta', show2=False)
#

turtle.exitonclick()
