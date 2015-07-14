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

#converts the number to a string, then goes through, converting that string back to an int (could have done a loop that does mod 10 to get the last digit
#then truncate, till left with one digit as well.
def sumDigits(theNum):
	stringVer = str(theNum)
	total = 0
	for num in stringVer:
		total += int(num)
	print total

#gets the list, gets the last digit(what we want, which is 100!)
#then sums all the digits and then prints it out
def main():
	listOfFactorials = populate(100)
	factorial = listOfFactorials[100]
	sumDigits(factorial)

main()