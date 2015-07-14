from datetime import date 

#idea, i searched and found that python has a date object library already done, so i imported that.
#The date object has a method call weekday() which returns what day of the week it is, 0 for monday 6 for sunday
#The idea was that I simply had to loop through the first of every month of every year, and did that through two for loops.
#Next all I had to do was make the date, run the weekday method, if it returned a 6 then it was a sunday and you incremented the count.
def main():
	startingYear = 1901
	startingMonth = 1
	count = 0
	for currentYear in range(startingYear, 2001):
		for currentMonth in range(startingMonth, 13):
			currentDay = date(currentYear, currentMonth, 1)
			numDay = currentDay.weekday()
			print currentDay
			print "NUM DAY IS: %i" % numDay
			if (numDay == 6):
				count = count + 1

	print count


main()