LIMIT = 4000000
sumOfEvens = 0
a = 1
b = 1
c = 2
# we know that every third term in the fibonnaci sequence is even. This makes sense because two odd numbers added together make an even number. 
while c < LIMIT:
	sumOfEvens += c 
	b = c + a 
	c = a + b 
print sumOfEvens

