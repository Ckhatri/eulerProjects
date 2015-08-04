#use dynamic programming to store previously values. recursive calls would take way too long.
#basically, in the populate method, store the previous factorial value, then you just have to do currVal * lastVal to get the factorial.
#much more efficient than writing it recursively where you'd do 8 * fact(7) which would call 7 * fact(6) and so on.

def populate(tgt):
	#0! is one, so add that to the list.
	pastVals = [1]
	for curVal in range(1, tgt + 1):
		currFactorial = curVal * pastVals[curVal-1]
		pastVals.append(currFactorial)
		# print currFactorial
	return pastVals

#goes through a number and sums up the factorials of its digits.
#if that total ever becomes greater than the original, than it returns False.
def digitFactorial(originalNumber, factorialList):
	total = 0
	number = originalNumber
	while number != 0:
		onesPlace = number % 10
		number = number / 10
		total += factorialList[onesPlace]
		if (total > originalNumber):
			return False
	return total == originalNumber

#gets the list of Factorials
#goes through from 1 to 100000 (didn't decide on a limit just arbitrary)
#if it follows the rule, aka the digits factorials add up the to original number, it adds it to a list so it can be stored/seen
#then goes through that list and sums it up
def main():
	listOfDigitFactorials = []
	total = 0
	listOfFactorials = populate(10)
	for currNumber in xrange(1,100000):
		if (digitFactorial(currNumber, listOfFactorials)):
			listOfDigitFactorials.append(currNumber)
	print listOfDigitFactorials
	for number in listOfDigitFactorials:
		total += number
	total -= 3
	print total


main()