
#goes through and adds digits to a list, if that digit is already in the list it shorts and doesn't add
def addDigitsToList(number, theList):
	while (number != 0):
		digitToAdd = number % 10
		if digitToAdd in theList or digitToAdd == 0: 
			return False
		theList.append(digitToAdd)
		number = number / 10
	return True

#takes the three numbers and then adds each of the digits to the list, if it returns true it returns the list of digits as well
def threeNumbers(firstNum, secondNum, multiple):
	listOfDigits = []
	if (addDigitsToList(firstNum, listOfDigits)):
		if (addDigitsToList(secondNum, listOfDigits)):
			if (addDigitsToList(multiple, listOfDigits)):
				return True, listOfDigits
	return False


def main():
	total = 0
	listOfProductsUsed = []
	for firstNum in xrange(1, 2000):
		for secondNum in xrange(1, 2000):
			multiple = firstNum * secondNum
			working = threeNumbers(firstNum, secondNum, multiple)
			if(working):
				#only adds the ones that have a length of 9 equal so theyre pandigal
				if (len(working[1]) == 9):
					pair = [firstNum, secondNum, multiple]
					#makes sure that the multiple hasn't already been found.
					if (multiple not in listOfProductsUsed):
						listOfProductsUsed.append(multiple)
						total += multiple
	print total


main()

