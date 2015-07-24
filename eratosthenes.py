def sieveOfEratosthenes(limit):
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
			prime_list.append(x)
			#go through each multiple of the value and set that to false
			for y in range(x + x, limit + 1, x): 
				sieve_list[y] = False
	return prime_list
