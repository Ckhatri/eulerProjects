import math
import time

# checks to see if the a and p given will be a solution. 
# a^2 + b^2 = c^2 can be rewritten to be a^2 + b^2 = (p-a-b)^2 = p^2 + a^2 + b^2-2pa-2pb+2ab
# so we can get b = (p^2-2ap)/(2p-2a)
# b must be an integer so, % == 0 will mean b is an integer.
def isSolution(a, p):
	return (p*p - 2*a*p) % (2*p-2*a) == 0


def main():
	maxCount = 0
	pMax = 0
	for p in range(120, 1000):
		count = 0
		for a in range(1, p/3):
			if isSolution(a, p):
				count += 1
		if count > maxCount:
			maxCount = count
			pMax = p
	print maxCount
	print pMax


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))