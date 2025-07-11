# Finds the number of integers 1 < n < 10^7 for which n and n+1 have the same
# number of divisors

import time
import math

start = time.time()

limit = 10**7
num_divisors = [0]*(limit + 1)

# We only need to check divisors up to the square root of the limit since we
# know that for each divisor we find belows the square root there will be
# another above it
for i in range(2,int(math.sqrt(limit)) + 1):
    # Special case for when the divisor is the square root
    num_divisors[i*i] += 1
    for j in range(i*i + i, limit + 1, i):
        num_divisors[j] += 2

total = sum(num_divisors[i] == num_divisors[i - 1] for i in range(3,limit))

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
