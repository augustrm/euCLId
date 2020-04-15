from euCLId import *
make_background("white")
seac.color("blue")
colormarker = euPoint(-300,300)
seac.color("black")

#We follow Euclid's construction of a regular pentagon within a given circle from his "Elements"
A = euPoint(0,0)
B = euPoint(200, 0)
seac.color("red")
AB = euLine(A,B)
seac.color("gray")
perpA = perpendicular(A, AB, show_line=False)
perpB = perpendicular(B, AB, show_line=False)
seac.color("black")
circAB = euCircle(A,B)
seac.color("gray")
circBA = euCircle(B,A)
_ignore, C = intersect(perpA, circAB)
_ignore , D = intersect(perpB, circBA)
AC = euLine(A,C)
BD = euLine(B,D)
CD = euLine(C,D)
E = midpoint(AC)
BE = euLine(B,E)
circEB = euCircle(E,B)
F, _ignore = intersect(perpA, circEB)
AF = euLine(A,F)
perpF = perpendicular(F, perpA, show_line=False)
G, _ignore = intersect(perpF, euCircle(F,A))
FG = euLine(F,G)
H = intersect(AB, perpendicular(G, FG, show_line=False))
GH = euLine(G,H)
M_AB = midpoint(AB)
_ignore, I = intersect(AB, euCircle(M_AB, H))
circBI = euCircle(B, I)
J, _ignore = intersect(circAB, circBI, show2=False)
seac.color("red")
BJ = euLine(B,J)
AJ = euLine(A,J)
seac.color("gray")
M_AJ = midpoint(AJ)
perp_M_AJ=perpendicular(M_AJ, AJ, show_line=False)
perp_M_AB = perpendicular(M_AB, AB, show_line=False)
CENT = intersect(perp_M_AJ, perp_M_AB)
BIGCIRC = euCircle(CENT, A)
bi_ABJ = angle_bisector(A,B,J, produce_line=True)
bi_AJB = angle_bisector(A,J,B, produce_line=True)
_ignore, X = intersect(BIGCIRC, bi_ABJ)
Y, _ignore = intersect(BIGCIRC, bi_AJB)
#Pentagon is defined by ABJXY
seac.color("red")
seac.pensize(3)
AX = euLine(A,X)
XJ = euLine(X,J)
JB = euLine(J,B)
BY = euLine(B,Y)
YA = euLine(Y,A)


screen.exitonclick()