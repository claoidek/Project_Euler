# Finds the value of d<1000 for which 1/d contains the longest recurring cycle in its
# decimal fraction part.
# This code works on the basis that for any prime d>5, the length of the decimal
# expansion will be the smallest n for which (10^n - 1)%d == 0.

import time

def is_prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
            return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

start = time.clock()

max_period = 0
max_value = 0

for d in range(7, 1000):
    if is_prime(d):
        exponent = 1
        while (10**exponent - 1)%d != 0:
            exponent += 1
        if exponent > max_period:
            max_period = exponent
            max_value = d


end = time.clock()

print max_value
print "Time taken: ", end-start, " s"
