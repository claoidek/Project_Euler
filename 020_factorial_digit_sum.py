# Finds the sum of the digits of 100!

from time import clock
import math

start = clock()

answer = sum(int(i) for i in str(math.factorial(100)))

end = clock()

print answer
print "Time taken: ", end-start, " s"
