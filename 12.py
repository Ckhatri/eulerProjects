import math

#this will give you a list of numberOfTri triangular numbers.
def triangularNumber(numbersOfTri):
	listOfTriNumbers = []
	for n in range(numbersOfTri):
		currentNum = (n*(n+1)) / 2
		listOfTriNumbers.append(currentNum)

#this will give you a specific triangular number for n such as the 100th triangular number
def triangleNumberN(n):
	return (n*(n+1)) / 2

#this will find all the factors of that triangular number.
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

#this runs the code to find what the actual triangle number is that works for this problem. It wants 500 factors

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


# t = 1 #triangle number
# a = 1
# count = 0
# while count <= 500:
# 	count = 0
# 	a = a+1
# 	t = t+a
# 	for x in range(1, t+1):
# 		if t % x == 0:
# 			count += 1
# print t




