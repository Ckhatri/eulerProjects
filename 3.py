import eratosthenes

#finds all primes less than 10000, could do whatever.
def main():
	biggestPrimeFactor = 0
	theListOfPrimes = eratosthenes.sieve(10000)
	for number in theListOfPrimes:
		#if a prime in the list divides the its now the biggestPrimeFactor
		if (600851475143 % number == 0):
			biggestPrimeFactor = number
	print biggestPrimeFactor


main()
