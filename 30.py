#assuming that if a n is 5 for the power
#must find an upper bound otherwise we could go forever -> largest could be 9^5 * 5 = limit
#after that it's just brute force checking.
from math import pow

#checks to see if the number's digits can be added to the fifth power to equal the original number
#returns if that is true or not.
def isNarcissistic(number):
	sum = 0
	originalNumber = number
	while (number != 0):
		currentDigit = number % 10
		powerVal = pow(currentDigit, 5)
		sum += powerVal
		number = number / 10
	intSum = int(sum)
	return originalNumber == sum

def main():
	total = 0
	narcisticList = []
	limit = int(pow(9, 5) * 5)
	for number in range(2, limit):
		if (isNarcissistic(number)):
			narcisticList.append(number)
	print narcisticList
	for number in narcisticList:
		total += number
	print total
main()
