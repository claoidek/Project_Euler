# Finds the sum of the digits of 100!

import time
import math

start = time.time()

answer = sum(int(i) for i in str(math.factorial(100)))

end = time.time()

print(answer)
print("Time taken: ", end-start, "s", sep="")
