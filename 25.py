def lastFibLength(fibs):
	lastVal = fibs[len(fibs) - 1]
	strVer = str(lastVal)
	return len(strVer) < 1000

def main():
	#need to start with the first two fibonacci numbers, which are both 1
	fibs = [1, 1]
	#if the last fib value is less than four digits, keep going
	while (lastFibLength(fibs)):
		firstVal = fibs[len(fibs) - 2]
		secondVal = fibs[len(fibs) - 1]
		newestVal = firstVal + secondVal
		fibs.append(newestVal)
	#now print the length, which will give the position
	print len(fibs)

main()
	
