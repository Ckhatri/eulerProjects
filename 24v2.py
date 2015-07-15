import itertools

#python has it built in wow easy
permutations = itertools.permutations("0123456789")

count = 0
for permutation in permutations:
	if (count == 1000000):
		print permutation
	count+=1


