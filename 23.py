import math

def divisors(num):
	total = 0
	#to find all the divisors for a number, you need to go from 1 to the sqrt of that number (since you can find pairs)
	for div in range(1, int(math.sqrt(num)) + 1):
		if (num % div == 0):
			#add the pair to the list
			total += div
			#don't want to add the same divisor twice.
			if (num / div != div):
				total += num / div
	#proper divisors are all numbers less than n, so 1 would find the the number itself, does you need to subtract the number itself from the sum.
	total -= num
	return total


def abundantNumFinder():
	abundantList = []
	for num in range(12, 28123):
		numsTotal = divisors(num)
		if (numsTotal > num):
			abundantList.append(num)
	return abundantList

def main():
	total = 0
	maxNumber = 28123
	canBeWrittenWithAbundants = [False] * maxNumber
	abundantList = abundantNumFinder()
	for num in range(0, len(abundantList)):
		firstVal = abundantList[num]
		for secondNum in range(num, len(abundantList)):
			secondVal = abundantList[secondNum]
			theSum = firstVal + secondVal
			if (theSum < maxNumber):
				canBeWrittenWithAbundants[theSum] = True
	for pos in range(0, maxNumber):
		val = canBeWrittenWithAbundants[pos]
		if (val == False):
			total += pos
	print total

main()
