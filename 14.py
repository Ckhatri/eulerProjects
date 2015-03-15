
#counts the number in each chain
def findChain(startingNumber):
	currentNumber = startingNumber
	count = 1
	while (currentNumber != 1):
		if currentNumber % 2 == 1:
			currentNumber = 3 * currentNumber + 1
		else:
			currentNumber = currentNumber / 2
		count += 1
	return count

#goes through from 100K to 1Mil and finds the one with the maximum number in the chain
def main():
	startingNumber = 100000
	upperLimit = 1000000
	theMax = 0
	theNumberOfMax = 0
	for n in range(startingNumber, upperLimit):
		theCount = findChain(n)
		if (theCount > theMax):
			theMax = theCount
			theNumberOfMax = n
	print theNumberOfMax

main()