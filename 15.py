import math

#knowing that lattice parts are combinatorics going from (0, 0) to (2, 2) then the formula is (a + b)C(b) which is equal to (a+b)!/(b! * (a)!)

def findNumPaths(dimension):
	a = dimension
	theNuMPaths = math.factorial(a + a) / ((math.factorial(a) * math.factorial(a)))
	print theNuMPaths

findNumPaths(20)