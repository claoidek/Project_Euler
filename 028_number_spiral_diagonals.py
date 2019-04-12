# Finds the sum of all numbers along both diagonals in a 1001x1001 spiral
# centred at 1.
#
# Example of a 5x5 spiral:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

from time import clock

start = clock()

spiral_width = 1001
current_width = 3
current_number = 1
total = 1

while current_width <= spiral_width:
    total += current_number*4 + current_width*10 - 10
    current_number += current_width*4 - 4
    current_width += 2

end = clock()

print total
print "Time taken: ", end-start, " s"
