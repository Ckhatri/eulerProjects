def sumOfSquares(numSquares):
	theSum = 0
	for n in range(numSquares + 1):
		theSum += (n * n)
	return theSum

def squareOfSum(numVals):
	theSum = 0
	for n in range(numVals + 1):
		theSum += n
		
	theSum = theSum * theSum
	return theSum

def main():
	print squareOfSum(100) - sumOfSquares(100) 

main()

