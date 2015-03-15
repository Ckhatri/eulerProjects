def multOfThreeOrFive(limit):
	total = 0
	for i in range (limit):
		if (i % 3 == 0 or i % 5 == 0):
			total += i

	print total

multOfThreeOrFive(1000)