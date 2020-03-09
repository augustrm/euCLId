from euCLId import *

seac.color("black")

A, B, C, D = euPoint(-200,-100), euPoint(0,-100), euPoint(0, 100), euPoint(-200, 100)
E = euPoint(200, -100)
AB, BC, CD, DA = euLine(A,B), euLine(B,C), euLine(C,D), euLine(D,A) 
BE = euLine(B,E)
circBA = euCircle(B,A)
circAB = euCircle(A,B)
ignore ,G = intersect(circAB, circBA, show1=False)
circEG = euCircle(E,G)
_ignore, F = intersect(circEG, AB)
circBF = euCircle(B,F)
H, _ignore1 = intersect(circBF, BC)
seac.color("red")
seac.pensize(2)
DF, FH, DH = euLine(D,F), euLine(F,H), euLine(D,H)
turtle.exitonclick()