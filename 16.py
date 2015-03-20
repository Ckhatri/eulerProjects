import math

def sumDigits(theValue):
	stringVer = str(theValue)
	theSum = 0
	#loops through and gets each char, and then adds that to the total sum after converting it to an int.
	for pos in range(len(stringVer)):
		theInt = int(stringVer[pos])
		theSum += theInt
	print theSum


def main():
	theValue = pow(2, 1000)
	sumDigits(theValue)

main()