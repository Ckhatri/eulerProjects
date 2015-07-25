#idea for this is to calculate the values, and put them into a set which will do the repeats removed for us.
#next its asking for the number of distinct values, so that's easily done by just printing out the final length

from sets import Set
from math import pow

def main():
	numbers = Set()
	for a in range (2, 101):
		for b in range (2, 101):
			numCalculated = pow(a, b)
			numbers.add(numCalculated)
	print len(numbers)

main()
