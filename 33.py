#follows the rules given on the project
def cancelDigits(numerator, denominator):
	numSecondDigit = numerator % 10
	numFirstDigit = numerator / 10
	denSecondDigit = denominator % 10
	denFirstDigit = denominator / 10
	newFrac = -1
	#make sure no dvision by zero occurs
	if (numSecondDigit == denFirstDigit and numFirstDigit != 0 and denSecondDigit != 0):
		currentFrac = float(numerator) / denominator
		newFrac = float(numFirstDigit) / denSecondDigit
		return currentFrac == newFrac and currentFrac != 1

def main():
	product = 1
	for numerator in xrange(10,100):
		for denominator in xrange(10,100):
			#finds the product
			if (cancelDigits(numerator, denominator)):
				product *= (float(numerator) / denominator)
	print product
	#at this point i semi cheated and realized 0.01 is just 1/100 so the answer was a hundred

main()