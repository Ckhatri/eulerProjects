import eratosthenes
from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect

def main():
	sumVals = 0
	count = 0
	listOfPrimes = eratosthenes.sieveOfEratosthenes(1000000)
	for prime in listOfPrimes:
		if(truncatedLeftPrime(prime, listOfPrimes)):
			if (truncatedRightPrime(prime, listOfPrimes)):
				sumVals += prime
	#2, 3, 5, 7 aren't considered truncatabled primes, must subtract
	sumVals -= (2 + 3 + 5 + 7)
	print sumVals
	
		

#truncates left
def truncateLeft(value):
	truncatedVal = value % pow(10, len(str(value)) - 1)
	return truncatedVal

#truncates right by diviing by ten
def truncateRight(value):
	truncatedVal = value / 10
	return truncatedVal

#keeps truncating the value until either it finishes and the value is prime and returns true or until it becomes not prime.
def truncatedLeftPrime(value, listOfPrimes):
	while (value != 0):
		#binary search
		pos = bisect_left(listOfPrimes, value)
		pos2 = bisect_right(listOfPrimes, value)
		if (pos == pos2):
			return False
		value = truncateLeft(value)
	return True

#same as above, except truncates right.
def truncatedRightPrime(value, listOfPrimes):
	while (value != 0):
		pos = bisect_left(listOfPrimes, value)
		pos2 = bisect_right(listOfPrimes, value)
		if (pos == pos2):
			return False
		value = truncateRight(value)
	return True
			
main()