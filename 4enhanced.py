def reverse(n):
	reverse = 0
	while n > 0:
		reverse = 10*reverse + n%10
		n = n/10
	return reverse

def isPalindrome(n):
	return n == reverse(n)

# if multiplying two three digit numbers
# let x,y,z be the digits.
# form must be 100000x+10000y+1000z+100z+10y+x
# which equals 100001x+10010y+1100z = 11(9091x+910y+100z)
# since 11 is prime, either a or b must be factors of 11

largestPalindrome = 0
a = 999 #start from larger numbers, easier to break out.
while a >= 100:
	if a % 11 == 0:
		b = 999
		db = 1
	# know b must be divisible by 11 if a is not.
	else:
		b = 990 #largest number divisible by 11, below 999
		db = 11
	keepSearching = True
	while (b >= a and keepSearching):
		multNum = a*b
		# if mult num is less than the largest palindrome we can finish no need to keep checking.
		if multNum <= largestPalindrome:
			keepSearching = False
		if isPalindrome(multNum):
			largestPalindrome = multNum
		b = b - db
	a = a-1

print largestPalindrome


