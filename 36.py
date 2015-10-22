def main():
	sum = 0
	for x in xrange(1,1000000):
		if(isPalindrome(str(x))):
			binString = toBinary(x)
			if (isPalindrome(binString)):
				sum += x
	print(sum)

def isPalindrome(token):
	lenOfToken = len(token)
	pos1 = 0
	pos2 = lenOfToken - 1
	while(pos1 < lenOfToken / 2):
		if (token[pos1] != token[pos2]):
			return False
		pos1 += 1
		pos2 -= 1
	return True

def toBinary(value):
	binaryString = ""
	while (value != 0):
		bitLeft = value % 2
		binaryString = str(bitLeft) + binaryString
		value = value / 2
	return binaryString

main()