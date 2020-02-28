from euCLId import *
from numpy import linspace
N = 50
Ns = linspace(-295, -100.1, N)

seac.color("#adadad")


A = euPoint(-500,0)
O = euPoint(-300,0)
B = euPoint(-100,0)

AB = euLine(A,B, produce=True)
circle = euCircle(O,A)

points_on_circle = []
for i in Ns:
	first, second = intersect(perpendicular(euPoint(i,0, show=False),AB, show_line=False),circle, show2=False)
	points_on_circle.append(first)

hyperbola_points = []
for j in points_on_circle:
	radial_line = euLine(O,j, show=False)
	tan = perpendicular(j, radial_line, show_line=False)
	AB_inter = intersect(tan, AB)
	clean_tangent = euLine(j,AB_inter)
	perp_to_AB = perpendicular(AB_inter, AB, show_line=False)
	paral = parallel(j, AB, show_line=False)
	hyperbola_point = intersect(perp_to_AB, paral)
	clea_paral = euLine(j, hyperbola_point)
	hyperbola_points.append(hyperbola_point)

seac.color("red")
seac.pensize(5)
for k in range(0, len(hyperbola_points)-1):
	#print(k, len(hyperbola_points))
	linkage = euLine(hyperbola_points[k], hyperbola_points[k+1])



turtle.exitonclick()
