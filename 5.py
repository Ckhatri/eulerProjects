def checkDivThrough20(number):
	divisable = True
	for n in range (1, 21):
		if (number % n != 0):
			divisable = False
			return divisable
	return divisable

#takes forever not efficient
def findSmallestPosNumber():
	notFound = True
	currentNum = 1000
	while notFound:
		if (checkDivThrough20(currentNum)):
			notFound = False
		else:
			currentNum += 1
			print currentNum
	print currentNum

def main():
	findSmallestPosNumber()

main()
