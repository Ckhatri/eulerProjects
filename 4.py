def palindromeChecker(number):
	#we know this is a six digit number.
	stringVer = "%d" % number
	#this starts at the end, and thus reverses the number.
	#if its a palindrome they should be the same.
	reversedVer = stringVer[::-1]
	return (stringVer == reversedVer)

def findBiggestPalindrome():
	biggestPalindrome = 0
	#goes through all the triple digit multiples
	for n in range (100, 1000):
		for i in range (100, 1000):
			mult = n * i
			#if its a palindrome and bigger than current biggestPalindrome
			if palindromeChecker(mult) and mult > biggestPalindrome:
				biggestPalindrome = mult
	print biggestPalindrome

def main():
	findBiggestPalindrome()


print main()