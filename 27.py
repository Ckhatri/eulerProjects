#first let us generate a list of primes, so that we can then check.
#brute force, slow but within a minute

import eratosthenes

# def isPrime(number):
# 	listOfPrimes = eratosthenes.sieveOfEratosthenes(10000)
# 	pos = 0
# 	while (number >= listOfPrimes[pos]):
# 		if (listOfPrimes[pos] == number):
# 			return True
# 		pos += 1
# 	return False


def calculate(a, b, n):
	return (n*n + a * n + b)

def main():
	bestA = 0
	bestB = 0
	bestN = 0
	listOfPrimes = eratosthenes.sieveOfEratosthenes(10000)
	for a in xrange(-1000, 1000):
		for b in xrange(-1000, 1000):
			n = 0
			while (calculate(a, b, n) in listOfPrimes):
				n+= 1
			if (n > bestN):
				bestA = a
				bestB = b
				bestN = n
	print bestA * bestB

main()



