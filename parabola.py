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
	################
	#print(j.xy)
	################
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

"""
_subE2 = euPoint(-190,0)
_subE1 = euPoint(-180,0)
E = euPoint(-175,0)
F = euPoint(-100, 0)
G = euPoint(-50,0)
H = euPoint(0,0)
I = euPoint(50,0)
J = euPoint(75,0)
K = euPoint(200,0)
L = euPoint(390,0)

perpAB_E2 = perpendicular(_subE2,AB, produce_line=True)
perpAB_E1 = perpendicular(_subE1,AB, produce_line=True)
perpAB_E = perpendicular(E,AB, produce_line=True)
perpAB_F = perpendicular(F,AB, produce_line=True)
perpAB_G = perpendicular(G,AB, produce_line=True)
perpAB_H = perpendicular(H,AB, produce_line=True)
perpAB_I = perpendicular(I,AB, produce_line=True)
perpAB_J = perpendicular(J,AB, produce_line=True)
perpAB_K = perpendicular(K,AB, produce_line=True)
perpAB_L = perpendicular(L,AB, produce_line=True)

seac.color("red")
circAE2 = euCircle(midpoint(A,_subE2, show_point=False), A)
circAE1 = euCircle(midpoint(A,_subE1, show_point=False), A) 
circAE = euCircle(midpoint(A,E, show_point=False), A)
circAF = euCircle(midpoint(A,F, show_point=False), A)
circAG = euCircle(midpoint(A,G, show_point=False), A)
circAH = euCircle(midpoint(A,H, show_point=False), A)
circAI = euCircle(midpoint(A,I, show_point=False), A)
circAJ = euCircle(midpoint(A,J, show_point=False), A)
circAK = euCircle(midpoint(A,K, show_point=False), A)
circAL = euCircle(midpoint(A,L, show_point=False), A)

seac.color("blue")
_subN1 , _subN2 = intersect(circAE2, perpAB_D)
_subM1 , _subM2 = intersect(circAE1, perpAB_D)
M1, M2 = intersect(circAE, perpAB_D)
N1, N2 = intersect(circAF, perpAB_D)
O1, O2 = intersect(circAG, perpAB_D)
P1, P2 = intersect(circAH, perpAB_D)
Q1, Q2 = intersect(circAI, perpAB_D)
R1, R2 = intersect(circAJ, perpAB_D)
S1, S2 = intersect(circAK, perpAB_D)
T1, T2 = intersect(circAL, perpAB_D)

seac.color("green")
perpsubN1 , perpsubN2 =  perpendicular(_subN1, perpAB_D, produce_line=True), perpendicular(_subN2, perpAB_D, produce_line=True)
perpsubM1 , perpsubM2 =  perpendicular(_subM1, perpAB_D, produce_line=True), perpendicular(_subM2, perpAB_D, produce_line=True)
perpM1, perpM2 = perpendicular(M1, perpAB_D, produce_line=True), perpendicular(M2, perpAB_D, produce_line=True)
perpN1, perpN2 = perpendicular(N1, perpAB_D, produce_line=True), perpendicular(N2, perpAB_D, produce_line=True)
perpO1, perpO2 = perpendicular(O1, perpAB_D, produce_line=True), perpendicular(O2, perpAB_D, produce_line=True)
perpP1, perpP2 = perpendicular(P1, perpAB_D, produce_line=True), perpendicular(P2, perpAB_D, produce_line=True)
perpQ1, perpQ2 = perpendicular(Q1, perpAB_D, produce_line=True), perpendicular(Q2, perpAB_D, produce_line=True)
perpR1, perpR2 = perpendicular(R1, perpAB_D, produce_line=True), perpendicular(R2, perpAB_D, produce_line=True)
perpS1, perpS2 = perpendicular(S1, perpAB_D, produce_line=True), perpendicular(S2, perpAB_D, produce_line=True)
perpT1, perpT2 = perpendicular(T1, perpAB_D, produce_line=True), perpendicular(T2, perpAB_D, produce_line=True)

seac.color("black")
parasubF1, parasubF2 = intersect(perpsubN1, perpAB_E2), intersect(perpsubN2, perpAB_E2)
parasubE1, parasubE2 = intersect(perpsubM1, perpAB_E1), intersect(perpsubM2, perpAB_E1)
paraE1, paraE2 = intersect(perpM1, perpAB_E), intersect(perpM2, perpAB_E)
paraF1, paraF2 = intersect(perpN1, perpAB_F), intersect(perpN2, perpAB_F)
paraG1, paraG2 = intersect(perpO1, perpAB_G), intersect(perpO2, perpAB_G)
paraH1, paraH2 = intersect(perpP1, perpAB_H), intersect(perpP2, perpAB_H)
paraI1, paraI2 = intersect(perpQ1, perpAB_I), intersect(perpQ2, perpAB_I)
paraJ1, paraJ2 = intersect(perpR1, perpAB_J), intersect(perpR2, perpAB_J)
paraK1, paraK2 = intersect(perpS1, perpAB_K), intersect(perpS2, perpAB_K)
paraL1, paraL2 = intersect(perpT1, perpAB_L), intersect(perpT2, perpAB_L)
"""
turtle.exitonclick()