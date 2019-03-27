# Finds the number of combinations of r and n, where 1<=n<=100 and r<=n such
# that nCr > 1000000

import time
import math

def nCr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

start = time.clock()

total = 0

# We're told that the first combination to exceed one million has n=23, so we
# start from there
for n in range(23,101):
    # nCr has a binomial distribution, which is symmetric, so we only need to
    # check half the values of r
    # We check in reverse so that we can stop once one of the values is below
    # one million
    for r in range(n/2,-1,-1):
        if nCr(n,r) > 1000000:
            total += 2
        else:
            break
    # Account for double-counting if n is odd
    # NOTE: This method only works if for each n there is at least one r that
    # causes nCr to exceed one million
    # This is fine for this problem since we know that this is true for all
    # n>=23
    if n%2 == 1:
        total -= 1

end = time.clock()

print total
print "Time taken: ", end-start, " s"
