from euCLId import *
from numpy import linspace

N = 200
Ns = linspace(-295, -100.1, N)
#screen.bgcolor("#4a4a4a")
seac.color("black")


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
	arc_to_AB = euCircle(j, AB_inter, show=False)
	paral = parallel(j, AB, show_line=False)
	hyperbola_point, _ignore = intersect(arc_to_AB, paral, show2=False)
	clea_paral = euLine(j, hyperbola_point)
	hyperbola_points.append(hyperbola_point)

seac.color("red")
seac.pensize(4)
for k in range(0, len(hyperbola_points)-1):
	linkage = euLine(hyperbola_points[k], hyperbola_points[k+1])



turtle.exitonclick()
