#This file serves only as an entry point for the greater euCLId library
from euclid_macros import *

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def help():
	print("""
\033[1m\033[91m euPoint\033[0m (x, y, name=\"default euPoint name\", show=True) : 
A basic euclidean point.
Has attributes: self.xy , self.name, self.shape, self.show
Instances of this class are collected in the list euPoint.instances
Has Methods: .tikz()
Mandatory arguments: x and y coordinates, 
Optional arguments: name -> any string, show -> True/False
\n
\033[1m\033[91m euLine\033[0m (ptA, ptB, name="default euLine name", show=True, produce=False) :
A line segment, that may be PRODUCED to be infinite.
Has attributes: self.name, self.shape, self.ptA, self.ptB, self.show, self.slope
Instances of this class are collected in the list euLine.instances
Has Methods: .tikz()
Mandatory arguments: ptA -> some euPoint, ptB -> some euPoint
Optional arguments: name -> any string, show -> True/False, produce -> True/False
\n
\033[1m\033[91m euCircle\033[0m (center_point, radial_point, name="default euCircle name", show=True):
A circle defined by given center point and radial point.
Has attributes: self.name, self.shape, self.c, self.r_p, self.radius, self.show, 
Instances of this class are collected in the list euCircle.instances
Has Methods: .tikz()
Mandatory arguments: center_point -> euPoint, radial_point -> euPoint
Optional arguments: name -> any string, show -> True/False
\n
\033[1m\033[91m intersect\033[0m (obj1, obj2, name1=None, name2=None, show=True, show1=True, show2=True) :
Function for finding the intersect of two objects; works for all sane intersections
Mandatory arguments: obj1 -> euLine or euCircle, obj2 -> euLine or euCircle
Optional arguments
""")
if __name__ == "__main__":
	help()
