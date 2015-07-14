#first need to find all the proper divisors of a given number
#next go through and find which are amicable numbers
#add them all together for a total

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

def generateList(tgt):
	dictOfAmicables = {}
	amicableList = []
	for num in range(1, tgt):
		#add up the divisors of the current number and then the divisors of the curret number
		numTotal = divisors(num)
		secondTotal = divisors(numTotal)
		#if the secondTotal equals the original number means d(a) = b and d(b) = a but a != b, then add it to the list
		#note at this point, we can just add the number to the total, and find the answer in this method, but for resuabilty issues we'll
		#just return the list
		if secondTotal == num and numTotal != secondTotal:
			amicableList.append(num)
	return amicableList


def main():
	total = 0
	amicableList = generateList(10000)
	for number in amicableList:
		total += number
	print total

main()
