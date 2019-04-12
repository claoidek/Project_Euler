# Finds the difference between the sum of the squares and the square of the sum
# of the first 100 natural numbers

from time import clock

start = clock()

sum_square = 0
square_sum = 0

for i in range(1,101):
	sum_square += i*i
	square_sum += i

square_sum = square_sum*square_sum

end = clock()

print square_sum-sum_square
print "Time taken: ", end-start, " s"
