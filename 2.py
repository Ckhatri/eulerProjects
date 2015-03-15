def createFibonacci(limit):
	listOfFibo = []
	listOfFibo.append(1)
	listOfFibo.append(2)
	n = 2
	currentVal = 0
	#creates a fibonacci sequence until the limit given.
	while currentVal < limit:
		currentVal = listOfFibo[n - 2] + listOfFibo[n - 1]
		listOfFibo.append(currentVal)
		n += 1
	listOfFibo.pop()
	print listOfFibo
	return listOfFibo

#goes through a list and adds all the evens
def addEvens(theList):
	total = 0
	for number in theList:
		if (number % 2 == 0):
			total += number
	print total

def main():
	theList = createFibonacci(4000000)
	addEvens(theList)

main()