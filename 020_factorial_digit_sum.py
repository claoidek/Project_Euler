# Finds the sum of the digits of 100!

import time
import math

start = time.clock()

answer = sum(int(i) for i in str(math.factorial(100)))

end = time.clock()

print answer
print "Time taken: ", end-start, " s"
