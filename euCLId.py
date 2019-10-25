import turtle
from math import *
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


class euCircle:
    def __init__(self, center_point, radial_point, name, n=1000):
        self.name = name
        self.c = center_point
        self.r_p = radial_point
        self.radius = sqrt((self.r_p[0]-self.c[0])**2 + (self.r_p[1]-self.c[1])**2)

        thetas = []

        for i in range(n+1):
            thetas.append(pi/4 + ((pi/4)/n)*i)

        self.octant1 = []

        for theta in thetas:
            coordinate = (self.c[0]+(self.radius*cos(theta)), self.c[1]+(self.radius*sin(theta)))
            self.octant1.append(coordinate)
        self.circ_coords = []
        for j in self.octant1:
            self.circ_coords.extend([(j[0], j[1]), (j[1], j[0]), (j[1], -j[0]), (j[0], -j[1]), (-j[0], -j[1]), (-j[1], -j[0]), (-j[1], j[0]), (-j[0], j[1])])

        
       
        
        
        
testcirc = euCircle(A,B,"circAB", n=10)

def circthru(ptA, ptB):
	seac.setpos(ptB[0], ptB[1])
	seac.pd()
	seac.setheading(seac.towards(ptA)-90)
	radius=seac.distance(ptA)
	seac.circle(radius)
	seac.pu()

turtle.exitonclick()
