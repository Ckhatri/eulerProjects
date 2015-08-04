import eratosthenes

#if the number has an even digit in it, not all of its rotations wil be prime, so we can get rid of those primes.
#if the number has a 0 or a 5 in it, not all of its rotations will be prime, so we can get rid of those primes as well
#basically the only digits the circular prime can consist of are be 1, 3, 7, 9
def noEvenNumberPrime(number):
	while number != 0:
		onesDigit = number % 10
		number = number / 10
		if (onesDigit % 2 == 0 or onesDigit == 0 or onesDigit == 5):
			return False
	return True

#finds all rotations of a number's digits by cutting off the first value and adding it to the end of string of numbers
def circularPrimeChecker(number, listOfPrimes):
	stringVersion = str(number)
	lengthOfNumber = len(stringVersion)
	#if we let the for loop go to lengthOfNumber it'll check the original number, which we already know is prime
	for x in xrange(0,lengthOfNumber - 1):
		firstDigit = stringVersion[0]
		splitString = stringVersion[1:]
		newNumber = splitString + firstDigit
		intNewNumber = int(newNumber)
		#check to see if all rotations are prime
		if intNewNumber not in listOfPrimes:
			return False
		stringVersion = newNumber
	return True
def main():
	listOfPrimes = eratosthenes.sieveOfEratosthenes(1000000)
	listOfCircularPrimes = []
	#two will not pass this test, but it is prime, so manually add it.
	#also five will not pass the test given above, but it is prime, so add it.
	updatedListOfPrimes = [2, 5]
	#update the list of primes according to the criteria
	for number in listOfPrimes:
		if noEvenNumberPrime(number):
			updatedListOfPrimes.append(number)
	# now these numbers have no even digits
	# go through these numbers and check if they're circular
	for number in updatedListOfPrimes:
		if (circularPrimeChecker(number, updatedListOfPrimes)):
			listOfCircularPrimes.append(number)
	print len(listOfCircularPrimes)

main()