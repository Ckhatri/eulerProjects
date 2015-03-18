def findTriplet(sum):
	#knowing the formula a = 2mn, b = m^2 - n^2, c = m^2 + n^2
	#a + b + c = sum (in this case 1000)
	#substituting, 2mn + m^2 - n^2 + m^2 + n^2 = 2mn + 2m^2 = 2m(n + m) = sum, which equates to m(n + m) = sum / 2 
	#knowing that n = (sum / 2 - m^2) / m
	#knowing this we can use this formula to find the values of m and n. assuming m > n.
	halfTheSum = sum / 2.0
	notFound = True
	actualM = 0
	actualN = 0
	m = 1
	#go through each m value until you can find one combination that works and solves the equation
	while notFound:
		n = (halfTheSum - (m* m)) / m
		if (n < m and m % n == 0 and notFound):
			actualM = m
			actualN = int(n)
			notFound = False
		m += 1
	#now just apply the original formula in line 2 to find the triplets
	a = 2 * actualM * actualN
	b = (actualM*actualM) - (actualN*actualN)
	c = (actualM*actualM) + (actualN*actualN)
	#next print out the values multiplied together, as asked in the question.
	print a * b * c

findTriplet(1000)
