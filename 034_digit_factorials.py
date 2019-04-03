# Finds the sum of all numbers that are equal to the sum of their digits'
# factorials.
# This one is very slow, Technically it can run in a fraction of a time if the
# upper bound is set to ~50000, but I don't have a theoretical justification for
# a bound that low.

import time

def sum_of_factorials(n):
    return sum([factorials[int(x)] for x in str(n)])

start = time.clock()

# Precomputed factorials to save time
factorials = [1,1,2,6,24,120,720,5400,40320,362880]

total = 0

# Upper bound is set to 7*9! because for numbers with >7 digits the sum of
# factorials can never be greater than the number itself
for i in range(3,factorials[9]*7):
    if i == sum_of_factorials(i):
        total += i

end = time.clock()

print total
print "Time taken: ", end-start, " s"
