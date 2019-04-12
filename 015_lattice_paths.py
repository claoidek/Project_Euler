# Calculates the number of possible routes through a 20x20 grid when only down
# and right moves are allowed.
# This is equivalent to 40 choose 20, so we can use nCr
# (en.wikipedia.org/wiki/Combination)

from time import clock
import math

start = clock()

x = 20
y = 20

nCr = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))

end = clock()

print nCr
print "Time taken: ", end-start, " s"
