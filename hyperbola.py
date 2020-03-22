from euCLId import *
from numpy import linspace
import os

make_background("white")
N = 10
Ns = linspace(-295, -100.1, N)
#screen.bgcolor("#4a4a4a")
seac.color("red")


A = euPoint(-500,0)
O = euPoint(-300,0)
B = euPoint(-100,0)

make_eps("0".zfill(4), directory="hyp", convert=True)
seac.color("black")
AB = euLine(A,B, produce=True)

make_eps("1".zfill(4), directory="hyp", convert=True)

circle = euCircle(O,A)

make_eps("2".zfill(4), directory="hyp", convert=True)

points_on_circle = []
#count=0
for i in Ns:
	#count+=1
	first, second = intersect(perpendicular(euPoint(i,0, show=False),AB, show_line=False),circle, show2=False)
	points_on_circle.append(first)
	#filename= str(count)+"_points_on_circle.eps"
	#screen.getcanvas().postscript(file=filename)

make_eps("3".zfill(4), directory="hyp", convert=True)

hyperbola_points = []
counter=4
for j in points_on_circle:
	radial_line = euLine(O,j, show=False)
	tan = perpendicular(j, radial_line, show_line=False)
	AB_inter = intersect(tan, AB)
	clean_tangent = euLine(j,AB_inter)
	#
	make_eps(str(counter).zfill(4), directory="hyp", convert=True)
	#
	arc_to_AB = euCircle(j, AB_inter, show=False)
	paral = parallel(j, AB, show_line=False)
	seac.setpos(j.xy)
	degrees_angle_ABinter_j_hyperbolapoint = 360-seac.towards(AB_inter.xy)
	seac.color("blue")
	clean_arc_to_AB = euCircle(j,AB_inter,show=True, arc=degrees_angle_ABinter_j_hyperbolapoint)
	seac.color("black")
	#
	make_eps(str(counter+1).zfill(4), directory="hyp", convert=True)
	#
	hyperbola_point, _ignore = intersect(arc_to_AB, paral, show2=False)
	clean_paral = euLine(j, hyperbola_point)
	#
	make_eps(str(counter+2).zfill(4), directory="hyp", convert=True)
	#
	counter+=3
	hyperbola_points.append(hyperbola_point)

seac.color("red")
seac.pensize(4)
for k in range(0, len(hyperbola_points)-1):
	linkage = euLine(hyperbola_points[k], hyperbola_points[k+1])

make_eps(str(counter).zfill(4), directory="hyp", convert=True)

for i in range(0,20):
	counter+=1
	make_eps(str(counter).zfill(4), directory="hyp", convert=True)
#screen.getcanvas().postscript(file="TEST.eps")
screen.exitonclick()
