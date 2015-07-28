#recursion? I hate recursion...
#Lets use dynamic programming!

def createTable(denoms, limit):
	table = [[0 for x in range(limit+1)] for x in range(len(denoms))]
	#first row will be the 1pence which means that every column in row 1 can only be made one way, which is through the 1's. 
	for pos in range(len(table[0])):
		table[0][pos] = 1
	# for row in range(len(table)):
	# 	coinVal = denoms[row]
	# 	for col in range(limit+1):
	# 		# get the top value, and the proper value to the side using the algorithm
			
	# 		topVal = table[row-1][col]
	# 		sideVal = table[row][col - coinVal]
	return table

def main():
	coinValues = [1, 2, 5, 10, 20, 50, 100, 200]
	limit = 200
	table = createTable(coinValues, limit)
	for row in range(1, len(coinValues)):
		coinVal = coinValues[row]
		for col in range(limit + 1):
			topVal = table[row-1][col]
			#if the coinValue is greater than the column, aka the current value needed to be reached, than you just pull down the topValue
			if (coinVal > col):
				table[row][col] = topVal
			#else get he side value, which is to the left the value of the coin. add that with the top value to find how to get all ways to get a certain value
			#using certain coins
			else: 
				sideVal = table[row][col-coinVal]
				table[row][col] = topVal + sideVal
	print table


main()

