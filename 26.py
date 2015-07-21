def getRepetitive():
	#goes through all denoms from 2 to 1000, uses the long division method to get the correct digits.
	#next you take the length - 1 because the first digit is always 0
	#update as necessary
	mostDigits = 0
	biggestCycleDenom = 1
	for x in xrange(2,1000):
		digits = longDivisionTillRepeat(1, x)
		numDigits = len(digits) - 1
		if (numDigits > mostDigits):
			mostDigits = numDigits
			biggestCycleDenom = x
	print biggestCycleDenom


		
def longDivisionTillRepeat(numerator, denominator):
	digits = ""
	remainder = 0
	listOfRemainders = []
	#if the numerator isn't 0, aka it was evenly divisible, and the current remainder isn't already existing, than keep going to find repetitive
	#Why does this work? Because if you get the same remainder when you're doing long division, you'll be doing the same thing over and over.
	while (numerator != 0 and remainder not in listOfRemainders):
		listOfRemainders.append(remainder)
		remainder = numerator % denominator
		numerator = numerator / denominator
		digits += str(numerator)
		numerator = remainder * 10
	return digits


def main():
	getRepetitive()





main()