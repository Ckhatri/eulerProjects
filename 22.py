
#open the file, goes through and puts all the names into a list, then alphabetically sorts it.
def getList():
	nameFile = open('p022_names.txt', 'r')
	nameList = []
	for word in nameFile:
		nameList = word.split(',')

	sortedList = sorted(nameList)
	return sortedList

#calculates the value of a name
def calculateValue(word, pos):
	total = 0
	#'A' is worth 1, but ascii value is 65 so you have to subtract 64 to get the "right" value.
	valToSubtract = 64
	for letter in word:
		#each name in the list has quotes around it, so this takes care of that.
		if (letter != "\""):
			charIntVal = ord(letter)
			charIntVal -= valToSubtract
			total += charIntVal
	#pos starts at 0, but the first name should have rank 1, so add one
	total *= (pos + 1) 
	return total



def main():
	total = 0
	sortedList = getList()
	for pos in range(0, len(sortedList)):
		currentWord = sortedList[pos]
		valOfWord = calculateValue(currentWord, pos)
		total += valOfWord
	print total

main()