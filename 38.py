import time

# does the multiplications to create the concat number.
def formConcat(original, limit):
	stringVersion = ""
	for x in range(1, limit+1):
		product = original * x
		stringVersion += str(product)
	return int(stringVersion)

#goes through and adds digits to a list, if that digit is already in the list it short circuits and doesn't add.
def addDigitsToList(number, theList):
	while (number != 0):
		digitToAdd = number % 10
		if digitToAdd in theList or digitToAdd == 0: 
			return False
		theList.append(digitToAdd)
		number = number / 10
	return True

def isPandigital(number):
	listOfNums = []
	return addDigitsToList(number, listOfNums)

def main():
	#original number must be less than 5 digits, since n > 1
	#original number must start with a 9 to be the biggest.
	#original number can't be two digits only, then we'd get 8 digits or over
	#original number can't be three digits only, since then you get > 9.
	#thus must be four digits, when n = 2
	original = 9000
	limit = 2
	currLength = 0
	maxVal = 0
	while currLength <= 9:
		concatNumber = formConcat(original, limit)
		currLength = len(str(concatNumber))
		if currLength <= 9:
			if isPandigital(concatNumber):
				if concatNumber > maxVal:
					maxVal = concatNumber
		original += 1
	print maxVal

main()