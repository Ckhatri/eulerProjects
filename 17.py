singles = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4] #gives the letters for each single digit
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] #gives the letters in each teen digit
doubles = [6, 6, 5, 5, 5, 7, 6, 6] #gives the letters of doubles like twenty, thirty etc.



def findTeens(x):
	#gives the teens
	return teens[x - 10]

def findDoubles(x):
	#gets the far left digit letters
	theSum = doubles[(x / 10) - 2]
	#should be one digit now
	x = x % 10
	#returns the single digits letters
	theSum += singles[x]
	return theSum


def findHundreds(x):
	#will have at least a hundred
	theSum = 7
	#gives 1, 2, 3.. 9 hundred
	theSum += singles[x / 100]
	#cuts off the far left digit
	x = x % 100
	if(x > 19):
		theSum += findDoubles(x)
	elif (x > 9 and x < 20):
		theSum += teens[x - 10]
	else:
		theSum += singles[x]
	return theSum


def findUpTo(x):
	theSum = 0
	for n in range(x + 1):
		print "THIS IS THE number: %d" % n
		#hard coded the max is 1000
		if (n == 1000):
			theSum += 11
		elif (n > 99 and n < 1000 and n % 100 != 0):
			theSum += findHundreds(n) + 3
		#need this in case its just a hundred with no other digits other than in the hundreds place
		elif (n > 99 and n < 1000 and n % 100 == 0):
			theSum += findHundreds(n)
		elif (n > 19 and n < 100):
			theSum += findDoubles(n)
		elif (n > 9 and n < 20):
			theSum += findTeens(n)
		else:
			theSum += singles[n]
		print "THIS IS THE SUM: %d" % theSum
	print theSum

findUpTo(1000)








