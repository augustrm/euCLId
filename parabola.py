from euCLId import *

A = euPoint(-300, 0)
B = euPoint(300,0)
D = euPoint(-200,0)

AB = euLine(A,B)
perpAB_D = perpendicular(D,AB)

E = euPoint(-175,0)
F = euPoint(-100, 0)
G = euPoint(-50,0)
H = euPoint(0,0)
I = euPoint(50,0)
J = euPoint(75,0)
K = euPoint(200,0)
L = euPoint(250,0)

circAE = euCircle(midpoint(A,E), A)
circAF = euCircle(midpoint(A,F), A)
circAG = euCircle(midpoint(A,G), A)
circAH = euCircle(midpoint(A,H), A)
circAI = euCircle(midpoint(A,I), A)
circAJ = euCircle(midpoint(A,J), A)
circAK = euCircle(midpoint(A,K), A)
circAL = euCircle(midpoint(A,L), A)



turtle.exitonclick()