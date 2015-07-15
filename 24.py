#Let us implement the Johnson-Trotter Algorithm to list all permutations of a digits.
#http://www.cut-the-knot.org/Curriculum/Combinatorics/JohnsonTrotter.shtml

#first let us create a datastructure for the algorithm, in which each integer has a "direction" its facing such as left or right
#we shall use bool values to denote left/right. false is left, right is true.

"""
Initialize the first permutation with <1 <2 ... <n
while there exists a mobile integer
  find the largest mobile integer k
  swap k and the adjacent integer it is looking at
  reverse the direction of all integers larger than k
"""

#NOTE THIS SOLUTION W/ proper implementation of algorithm is VERY inefficient because of all the deepcopies having to be made.
import copy

class Number():
	"""docstring for Number"""
	def __init__(self, number, direction):
		self.num = number
		self.dir = direction
	def __str__(self):
		return "number: %s direction: %s" % (self.num, self.dir)

def initNum(limit):
	theNum = []
	for num in range(0, limit):
		currNumber = Number(num, False)
		theNum.append(currNumber)
	return theNum

#finds the largest mobile integer in the permutation
def mobilePos(currPerm):
	largestMobilePos = -1
	maxVal = -1
	for pos in range(0, 10):
		#get info for the curVal
		curNumber = currPerm[pos]
		curDir = curNumber.dir
		curVal = curNumber.num
		#if it's false, then direction is left, so check the number to the left
		#if it's smaller than the current, you've found your "largest" mobile integer so far
		#if its update the max val.
		if (curDir == False and pos != 0):
			adjNumber = currPerm[pos - 1]
			adjVal = adjNumber.num
			if (adjVal < curVal and curVal > maxVal):
				largestMobilePos = pos
				maxVal = curVal
		#if direction is True then its to the right, so do pos + 1 to get adj, then compare.
		elif (curDir == True and pos != 9):
			adjNumber = currPerm[pos + 1]
			adjVal = adjNumber.num
			if (adjVal < curVal and curVal > maxVal):
				largestMobilePos = pos
				maxVal = curVal
	return largestMobilePos

def toStringDebug(daList):
	stringVer = ""
	for number in daList:
		stringVer += str(number.num) + str(number.dir)
	print stringVer

def toString(daList):
	stringVer = ""
	for number in daList:
		stringVer += str(number.num)
	return stringVer

def main():
	permsList = []
	stringListVer = []
	initialVal = initNum(10)
	permsList.append(initialVal)
	largestMobilePos = mobilePos(initialVal)
	currVal = copy.deepcopy(initialVal)
	while (largestMobilePos != -1):
		#this part gets the largest mobile val and switches it.
		largestMobileVal = currVal[largestMobilePos]
		if (largestMobileVal.dir == False):
			adjVal = currVal[largestMobilePos - 1]
			tempVal = Number(adjVal.num, adjVal.dir)
			currVal[largestMobilePos - 1] = largestMobileVal
			currVal[largestMobilePos] = tempVal
		else:
			adjVal = currVal[largestMobilePos + 1]
			tempVal = Number(adjVal.num, adjVal.dir)
			currVal[largestMobilePos + 1] = largestMobileVal
			currVal[largestMobilePos] = tempVal
		#swaps directions, if necessary
		for val in currVal:
			if (val.num > largestMobileVal.num):
				val.dir = not val.dir
		#puts the new vals into the perms list, deepcopy to make a new memory reference, and continue
		permsList.append(currVal)
		oldVals = currVal
		currVal = copy.deepcopy(oldVals)
		largestMobilePos = mobilePos(currVal)
	for numbers in permsList:
		stringListVer.append(toString(numbers))
	sortedList = sorted(stringListVer)

main()
		