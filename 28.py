#first the idea was to find the quadratic formulas for the numbers in the diagonals.
#noticed that the top right diagonal was just squares 1 9 25 49 (i drew the square out further)
#This gives us (2n+1)^2 for the top right, then by subtracting the proper values we could find the other diagonals
#the four equations are 4n^2+4n+1, 4n^2-2n+1, 4n^2 + 1, and 4n^2 + 2n + 1
#totalling these all together you get 16n^2 + 4n + 4
#next you jst have to sum this up from 1 to 500, then add a + 1 to the end because all diagionals start with one.


def main():
	sum = 0
	for n in range(1, 501):
		sum += (16 * n * n + 4 * n + 4)
	sum += 1
	print sum

main()


