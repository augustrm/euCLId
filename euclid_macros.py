from euCLId_core import *

def midpoint(A,B=None, show_process=False):
	if A.shape == 'line':
		P,Q = A.ptA, A.ptB
		templinePQ = euLine(P,Q,show=show_process)
		tempcircPQ, tempcircQP = euCircle(P,Q, show=show_process), euCircle(Q,P, show=show_process)
		tempX, tempY = intersect(tempcircPQ, tempcircQP, show=show_process)
		templineXY = euLine(tempX, tempY, show=show_process)
		M = intersect(templinePQ, templineXY)
		return M

	elif A.shape == 'point' and B != None:
		templineAB = euLine(A,B,show=show_process)
		tempcircAB, tempcircBA = euCircle(A,B, show=show_process), euCircle(B,A, show=show_process)
		tempX, tempY = intersect(tempcircAB, tempcircBA, show=show_process)
		templineXY = euLine(tempX, tempY, show=show_process)
		M = intersect(templineAB, templineXY)
		return M

def angle_bisector(A,B,C,show_process=False):
	templineAB = euLine(A,B, show=show_process)
	templineBC = euLine(B,C, show=show_process)
	seac.setpos(B[0],B[1])
	R = min([seac.distance(A[0], A[1]), seac.distance(C[0],C[1])]) - 0.01
	#easy generic radial point:
	Rpoint = (B[0], B[1]+R)
	circBR = euCircle(B,Rpoint, show=show_process)
	X1 = intersect(circBR, templineAB, show=show_process)
	X2 = intersect(circBR, templineBC, show=show_process)
	bisector = euLine(B, midpoint(X1,X2))
	return bisector




def perpendicular(A,LINE, show_process=False):
	pass

if __name__ == "__main__":
	A = euPoint(0,0)
	B = euPoint(0,200)
	C = euPoint(-400,-300)
	#M = midpoint(A,B)
	#lineAC = euLine(A,C)
	#O = midpoint(lineAC, show_process=True)
	#seac.home()
	#lineOM = euLine(O,M)
	#lineMA = euLine(M,A)
	angle_bisector(A,B,C, show_process=True)
	turtle.exitonclick()