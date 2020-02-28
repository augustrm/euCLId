#This file serves only as an entry point for the greater euCLId library
from euclid_macros import *

def help():
	print("""
		\neuPoint(x, y, name=\"default euPoint name\", show=True) : 
		\nA basic euclidean point.
		\nMandatory arguments: x and y coordinates, 
		\nOptional arguments: name -> any string, show -> True/False
		\n
		\neuLine(ptA, ptB, name="default euLine name", show=True, produce=False) :
		\nA line segment, that may be PRODUCED to be infinite.
		\nMandatory arguments: ptA -> some euPoint, ptB -> some euPoint
		\nOptional arguments: name -> any string, show -> True/False, produce -> True/False
		\n
		\neuCircle(center_point, radial_point, name="default euCircle name", show=True):
		\nA circle defined by given center point and radial point.
		\nMandatory arguments: center_point -> euPoint, radial_point -> euPoint
		\nOptional arguments: name -> any string, show -> True/False

		""")
if __name__ == "__main__":
	help()
