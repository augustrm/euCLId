import turtle
from math import cos, sin, sqrt, pi

screen = turtle.Screen()
screen.setup(width=600,height=600,startx=None,starty=None)
screen.title("euCLId")
screen.screensize(2000,2000)
turtle.delay(10)
#stylistic note: seac stands for Straight Edge And Compass
seac = turtle.Turtle()
#seac.ht()
seac.speed(9)
seac.home()
seac.pu()
seac.color("red")

class euPoint:
	def __init__(self, x, y, name="default euPoint name", show=True):
		self.xy = (x,y)
		self.name = name
		self.shape = 'point'
		self.show = show
		# rolling "draw" functionality into class definitions
		if self.show == True:
			seac.pu()
			seac.setpos(self.xy[0], self.xy[1])
			seac.dot(7)
	def __iter__(self):
		yield(self.xy)
	def __getitem__(self, i):
		return self.xy[i]
	def __str__(self):
		return self.name

		
class euLine:
	def __init__(self, ptA, ptB, name="default euLine name", show=True, produce=False):
		self.name = name
		self.shape = 'line'
		self.ptA = (ptA[0], ptA[1])
		self.ptB = (ptB[0], ptB[1])
		self.show = show
		self.produce = produce
		# Conditional necessary to handle edge case of vertical and close to vertical lines:
		if self.ptB[0]-self.ptA[0] != 0:
			self.slope = (self.ptB[1] - self.ptA[1]) / (self.ptB[0] - self.ptA[0])
		else:
			self.slope = "vertical"
		# rolling depracated "draw_line()" method into euLine class:
		if self.show == True:
			if produce == False:
				seac.pu()
				seac.setpos(self.ptA[0], self.ptA[1])
				seac.pd()
				seac.setpos(self.ptB[0], self.ptB[1])
				seac.pu()
			elif produce == True:
				if self.slope == "vertical":
					seac.pu()
					seac.setpos(self.ptA[0], -0.5*screen.screensize()[1])
					seac.pd()
					seac.setpos(self.ptA[0], 0.5*screen.screensize()[1])
					seac.pu()
				else:
					seac.pu()
					# first term is screenbound, second term is Y value at screebound
					seac.setpos(-0.5*screen.screensize()[0], self.slope*(-0.5*screen.screensize()[0] - self.ptA[0]) + self.ptA[1])
					seac.pd()
					seac.setpos(0.5*screen.screensize()[0], self.slope*(0.5*screen.screensize()[0] - self.ptA[0]) + self.ptA[1])
					seac.pu()
	def __str__(self):
		return self.name

class euCircle:
	def __init__(self, center_point, radial_point, name="default euCircle name", show=True):
		self.name = name
		self.shape = 'circle'
		self.c = (center_point[0],center_point[1]) 
		self.r_p = (radial_point[0], radial_point[1])
		self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)
		self.show = show
		if self.show == True:
			seac.pu()
			seac.setpos(self.r_p[0], self.r_p[1])
			seac.setheading(seac.towards((self.c[0],self.c[1]))-90)
			#radius = seac.distance((self.ptA[0],ptA[1]))
			seac.pd()
			seac.circle(self.radius)
			seac.pu()
	def __str__(self):
		return self.name
			
########################################################################################################
#                                     end of basic object definitions                                  #
########################################################################################################

def intersect(obj1, obj2, name1=None, name2=None, show=True, show1=True, show2=True):
	# simple 2x2 determinant:
	def _2x2det(a,b,c,d):
		return (a*d)-(c*b)
	
	# modified signum function for circle-line / line-circle intersect clause:
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

			if show != True:
				show1 = False
				show2 = False
					
			if name1 == None:
				int_1 =  euPoint(x3, y3, name=obj1.name+"_intersect_"+obj2.name+"_1",show=show1)
			else:
				name1=str(name1) #sanitize name1 so it is always a string
				int_1 = euPoint(x3, y3, name=name1, show=show1)
			
			if name2 == None:
				int_2 =  euPoint(x4, y4, name=obj1.name+"_intersect_"+obj2.name+"_2",show=show2)
			else:
				name2=str(name2) #sanitize name2 so it is always a string
				int_2 =  euPoint(x4, y4, name=name2,show=show2)
			return int_1, int_2
			seac.home
	
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

		# conditional to handle case of line and circle not intersecting:
		if (((r**2)*(d_r**2))-D) >= 0:
			x_int1 = ((D * d_y + _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
			y_int1 = ((-D * d_x + abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
			x_int2 = ((D * d_y - _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
			y_int2 = ((-D * d_x - abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
			
			# 
			if show != True:
				show1 = False
				show2 = False

			if name1 == None:
				int_1 = euPoint(x_int1, y_int1, name=obj1.name+"_intersect_"+obj2.name+"_1",show=show1)
			else:
				name1=str(name1) #sanitize name1 so it is always a string
				int_1 = euPoint(x_int1, y_int1, name=name1, show=show1)
			
			if name2 == None:
				int_2 =  euPoint(x_int2, y_int2, name=obj1.name+"_intersect_"+obj2.name+"_1",show=show1)
			else:
				name2=str(name2) #sanitize name2 so it is always a string
				int_2 = euPoint(x_int2, y_int2, name=name2, show=show2)
			
			return int_1, int_2
			"""
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
			"""
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

		# conditional to handle case of line and circle not intersecting:
		if (((r**2)*(d_r**2))-D) >= 0:
			x_int1 = ((D * d_y + _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
			y_int1 = ((-D * d_x + abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
			x_int2 = ((D * d_y - _signum(d_y) * d_x * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - x_delta
			y_int2 = ((-D * d_x - abs(d_y) * sqrt((r**2 * d_r**2) - D**2))/d_r**2) - y_delta
			
			# 
			if show != True:
				show1 = False
				show2 = False

			if name1 == None:
				int_1 = euPoint(x_int1, y_int1, name=obj1.name+"_intersect_"+obj2.name+"_1",show=show1)
			else:
				name1=str(name1) #sanitize name1 so it is always a string
				int_1 = euPoint(x_int1, y_int1, name=name1, show=show1)
			
			if name2 == None:
				int_2 =  euPoint(x_int2, y_int2, name=obj1.name+"_intersect_"+obj2.name+"_1",show=show2)
			else:
				name2=str(name2) #sanitize name2 so it is always a string
				int_2 = euPoint(x_int2, y_int2, name=name2, show=show2)
			
			return int_1, int_2

	elif obj1.shape == 'line' and obj2.shape == 'line':
		# http://mathworld.wolfram.com/Line-LineIntersection.html
		x1, y1 = obj1.ptA[0], obj1.ptA[1]
		x2, y2 = obj1.ptB[0], obj1.ptB[1]
		x3, y3 = obj2.ptA[0], obj2.ptA[1]
		x4, y4 = obj2.ptB[0], obj2.ptB[1]
		x_line_int = (_2x2det(_2x2det(x1, y1, x2, y2), (x1-x2), _2x2det(x3, y3, x4, y4), (x3-x4)))/(_2x2det((x1-x2), (y1-y2), (x3-x4), (y3-y4)))
		y_line_int = (_2x2det(_2x2det(x1, y1, x2, y2), (y1-y2), _2x2det(x3, y3, x4, y4), (y3-y4)))/(_2x2det((x1-x2), (y1-y2), (x3-x4), (y3-y4)))
		
		if show != True:
				show1 = False
				show2 = False

		if name1 == None:
			return euPoint(x_line_int, y_line_int, obj1.name+"_intersect_"+obj2.name+"_1", show=show1)
		else:
			name1=str(name1) #sanitize name1 so it is always a string
			return euPoint(x_line_int, y_line_int, name1, show=show1)
	
if __name__ == "__main__":
	"""#testing:
	#define a point, its coordinates are arbitrary:
	A = euPoint(300,50, "A")
	#seac.setpos(A.xy)
	#seac.dot()

	#define a point, its coordinates are arbitrary:
	B = euPoint(20, -39, "B")
	#seac.setpos(B.xy)
	#seac.dot()

	C = euPoint(80, 130, "C")
	#seac.setpos(C.xy)
	#seac.dot()

	D = euPoint(80, -50, "D")
	#seac.setpos(D.xy)
	#seac.dot()

	lineAB = euLine(A,B, 'test')
	lineCD = euLine(C,D, 'test2')
	seac.color("blue")
	#draw_line(A,B)
	#draw_line(C,D)
	X =intersect(lineAB, lineCD, name1='gamma')
	circXA = euCircle(X,A,"circle")
	circAD = euCircle(A,D, "circle2")
	Q,R = intersect(circXA, circAD, name1="top", name2="bottom")
	lineQR = euLine(Q,R, name="test3")
	G = intersect(lineQR, lineAB)
	'''
	draw_circle(A,B, show=False)
	draw_circle(B,A, show=False)
	seac.color("red")
	draw_line(A,B)
	seac.color("blue")
	intersect(circAB, circBA, name1='E',show2=False)
	draw_line(E,A)
	seac.color("green")
	draw_line(E,B)
	seac.color("green")
	draw_circle(C,B)
	seac.color("red")
	draw_circle(C,A)
	seac.color("blue")
	draw_circle(C,E)
	intersect(circCE, lineAB, name1 ='beta', show1=False)
	intersect(lineEA, circCA, name1='delta', show2=False)
	#
	"""
	A = euPoint(0,0)
	B = euPoint(100,0)
	#C = euPoint(-200,-90)
#bisect = angle_bisector(A,B,C,show_process=True)
	AB = euLine(A,B)
	circ = euCircle((50,0),(200, 0))
	X,Y = intersect(circ, AB)
	print("X=",X.xy, " Y=",Y.xy)
	turtle.exitonclick()
