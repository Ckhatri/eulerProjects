# http://codeforces.com/problemset/problem/661/F
# hacky modification to my sieve of eratosthenes 
def sieveOfEratosthenes(startingVal, limit):
	#Create a list of all true statements for some limit where position equals the "number"
	sieve_list = [True] * (limit+1)
	sieve_list[0] = False #0 is not prime
	sieve_list[1] = False #1 s not prime
	prime_list = []
	num = 2 #2 is prime so that here.
	 #if the value is prime (true) right now then do the rest of this from 2 to the end
	for x in range(2, limit + 1):
		if sieve_list[x] == True:
			#if this number is true it is prime, thus you can add it to the list of primes.
			if (x >= startingVal and x <= limit):
				prime_list.append(x)
			#go through each multiple of the value and set that to false
			for y in range(x + x, limit + 1, x): 
				sieve_list[y] = False
	return prime_list


from sys import stdin, stdout
first, second = [int(x) for x in stdin.readline().rstrip().split()]
listOfPrimes = sieveOfEratosthenes(first, second)
stdout.write(str(len(listOfPrimes)) + "\n")
	