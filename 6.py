def sumOfSquares(numSquares):
	theSum = 0
	for n in range(numSquares + 1):
		theSum += (n * n)
	return theSum

#uses the summation formula, then squares it. Changes it from O(N) (brute force) to O(1)
def squareOfSum(numVals):
	theSum = (numVals * (numVals + 1)) / 2
	theSum = theSum * theSum
	return theSum

def main():
	print squareOfSum(100) - sumOfSquares(100) 

main()

