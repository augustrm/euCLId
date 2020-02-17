import euCLId as e
A = e.euPoint(30,50, "A")
e.seac.setpos(A.xy)
e.seac.dot()

#define a point, its coordinates are arbitrary:
B = e.euPoint(20, -39, "B")
e.seac.setpos(B.xy)
e.seac.dot()

C = e.euPoint(80, 130, "C")
e.seac.setpos(C.xy)
e.seac.dot()

D = e.euPoint(80, -50, "D")
e.seac.setpos(D.xy)
e.seac.dot()

e.draw_circle(A,B)

e.draw_circle(C,D)

print(globals())

e.turtle.exitonclick()