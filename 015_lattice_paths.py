# Calculates the number of possible routes through a 20x20 grid when only down
# and right moves are allowed.
# This is equivalent to 40 choose 20, so we can use nCr
# (en.wikipedia.org/wiki/Combination)

import time
import math

start = time.time()

x = 20
y = 20

nCr = math.factorial(x+y)//(math.factorial(x)*math.factorial(y))

end = time.time()

print(nCr)
print("Time taken: ", end-start, "s", sep="")
