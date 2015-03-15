import math

def triangularNumber(numbersOfTri):
	listOfTriNumbers = []
	for n in range(numbersOfTri):
		currentNum = (n*(n+1)) / 2
		listOfTriNumbers.append(currentNum)

def triangleNumberN(n):
	return (n*(n+1)) / 2

def findFactors(number):
	limit =  math.sqrt(number)
	limit = int(limit)
	listOfFactors = []
	count = 0
	for n in range (1, limit):
		if (number % n == 0):
			listOfFactors.append(n)
			listOfFactors.append(number / n)
			count += 2
	return count

def main():
	n = 100
	notFound = True
	while notFound:
		tri = triangleNumberN(n)
		count = findFactors(tri)
		if (count >= 500):
			notFound = False
		else:
			n += 1
	print triangleNumberN(n)


main()