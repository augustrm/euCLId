from euCLId import *
from numpy import linspace

seac.pensize(3)
seac.color("black")
A = euPoint(-250, 0)
B = euPoint(800,0)
D = euPoint(-200,0)

AB = euLine(A,B)
perpAB_D = perpendicular(D,AB, produce_line=True)

seac.pensize(1)


N = 20

Ns = linspace(D[0], B[0], N)
testpoints = []

for i in Ns:
	testpoints.append(euPoint(i,0))

# testpoints is now a list of euPoints used to generate the parabola

pointbuffer = [D,D]

for j in testpoints:
	perpAB_j = perpendicular(j, AB, produce_line=True)
	circle_Aj = euCircle(midpoint(A,j,show_point=False),A)
	j1,j2 = intersect(circle_Aj, perpAB_D)
	perp_j1 = perpendicular(j1, perpAB_D, produce_line=True)
	perp_j2 = perpendicular(j2, perpAB_D, produce_line=True)
	para_j1 = intersect(perp_j1, perpAB_j)
	para_j2 = intersect(perp_j2, perpAB_j)
	seac.color("red")
	seac.pensize(4)
	linkage_1 = euLine(pointbuffer[0], para_j1)
	linkage_2 = euLine(pointbuffer[1], para_j2)
	pointbuffer = []
	pointbuffer.append(para_j1)
	pointbuffer.append(para_j2)
	seac.color("black")
	seac.pensize(1)

screen.exitonclick()
