# Finds the number of reduced proper fractions with denominator <= 12000 that
# fall between 1/2 and 1/3

import time

# Uses the formula for finding consecutive terms of Farey sequences here:
# https://en.wikipedia.org/wiki/Farey_sequence#Next_term
# The implementation shown at that link has been modified as follows:
# We now return the length of the sequence, not the sequence itself
# We start and stop at specified values, instead of processing the entire
# sequence
def farey_function(n):
    a = 0
    b = 1
    # Start at 1/3
    c = 1
    d = 3
    # We subtract 2 because we don't want 1/2 or 1/3 to be included in the total
    count = -2
    # Stop when we get to 1/2
    while float(c)/d <= 0.5:
        k = (n + b)/d
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        count += 1
    return count

start = time.clock()

answer = farey_function(12000)

end = time.clock()

print answer
print "Time taken: ", end-start, " s"
