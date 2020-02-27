from euclid_core import *

def midpoint(A,B=None, show_process=False, show_point=True):
	if A.shape == 'line':
		P,Q = A.ptA, A.ptB
		templinePQ = euLine(P,Q,show=show_process)
		tempcircPQ, tempcircQP = euCircle(P,Q, show=show_process), euCircle(Q,P, show=show_process)
		tempX, tempY = intersect(tempcircPQ, tempcircQP, show=show_process)
		templineXY = euLine(tempX, tempY, show=show_process)
		M = intersect(templinePQ, templineXY, show=show_point)
		return M

	elif A.shape == 'point' and B != None:
		templineAB = euLine(A,B,show=show_process)
		tempcircAB, tempcircBA = euCircle(A,B, show=show_process), euCircle(B,A, show=show_process)
		tempX, tempY = intersect(tempcircAB, tempcircBA, show=show_process)
		templineXY = euLine(tempX, tempY, show=show_process)
		M = intersect(templineAB, templineXY, show=show_point)
		return M

def angle_bisector(A,B,C,show_process=False,produce_line=False ):
	###########################################################################
	#                    --------------------------------                     #
	#                   | CAUTION!!   UNDER CONSTUCTION! |                    #
	#                    --------------------------------                     #
	#                           |       |          |                          #
	#                           V       V          V                          #
	###########################################################################
	templineAB = euLine(A,B, show=show_process)
	templineBC = euLine(B,C, show=show_process)
	seac.setpos(B[0],B[1])
	R = min([seac.distance(A[0], A[1]), seac.distance(C[0],C[1])])
	#easy generic radial point:
	Rpoint = (B[0], B[1]+R)
	circBR = euCircle(B,Rpoint, show=show_process)
	X1, Y1 = intersect(circBR, templineAB, show=show_process, show1=show_process, show2=show_process)
	X2, Y2 = intersect(circBR, templineBC, show=show_process, show1=show_process, show2=show_process)
	# quick distance functions to decide on which of the 4 points returned by interesects is closest to points of interest:
	dA = lambda P : sqrt((P[0] - A[0])**2 + (P[1] - A[1])**2)
	dC = lambda P : sqrt((P[0] - C[0])**2 + (P[1] - C[1])**2)
	point_list = [X1,Y1,X2,Y2]
	X_true = sorted(point_list, key=dA)[0]
	Y_true = sorted(point_list, key=dC)[0]
	bisector = euLine(B, midpoint(X_true, Y_true), produce=produce_line)
	return bisector




def perpendicular(X,LINE, show_process=False, produce_line=False):
	if X.xy == LINE.ptA:
		tempcirc1 = euCircle(X, LINE.ptB,show=show_process)	
	else:
		tempcirc1 = euCircle(X, LINE.ptA,show=show_process)
	A,B = intersect(tempcirc1, LINE, show=show_process, show1=show_process, show2=show_process)
	templineAB = euLine(A,B,show=show_process)
	tempcircAB, tempcircBA = euCircle(A,B, show=show_process), euCircle(B,A, show=show_process)
	tempX, tempY = intersect(tempcircAB, tempcircBA, show=show_process, show1=show_process, show2=show_process)
	perpendicular = euLine(tempX, tempY, produce=produce_line)
	return perpendicular



if __name__ == "__main__":
	A = euPoint(0,0)
	B = euPoint(-300,-190)
	C = euPoint(200,0)
	#M = midpoint(A,B)
	lineAC = euLine(A,C)

	#O = midpoint(lineAC, show_process=True)
	#seac.home()
	#lineOM = euLine(O,M)
	#lineMA = euLine(M,A)
	#angle_bisector(A,B,C, show_process=True, produce_line=True)
	angle_bisector(B,A,C, show_process=False, produce_line=True)
	#angle_bisector(B,C,A, show_process=True, produce_line=True)
	#p = perpendicular(B, lineAC, produce_line=True)
	turtle.exitonclick()
