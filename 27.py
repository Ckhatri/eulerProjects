#first let us generate a list of primes, so that we can then check, if the numbers generated through the
#quadratic equation are actually prime


#n must start at 0 to be consecutive, so that means n^2 + an + b is just b which means b must be prime
#b must be some prime number below 1000, taking that into account you reduce the number of b's looped through

import eratosthenes


def calculate(a, b, n):
	return (n*n + a * n + b)

def main():
	bestA = 0
	bestB = 0
	bestN = 0
	listOfPrimes = eratosthenes.sieveOfEratosthenes(10000)
	listOfBPrimes = eratosthenes.sieveOfEratosthenes(1000)
	for a in xrange(-1000, 1000):
		for b in listOfBPrimes:
			n = 0
			while (calculate(a, b, n) in listOfPrimes):
				n+= 1
			if (n > bestN):
				bestA = a
				bestB = b
				bestN = n
	print bestA * bestB

main()



