# Finds the sum of all pairs of numbers where d(a) = b and d(b) = a
# d(a) is defined as the sum of all proper divisors of a

import time
import math

start = time.clock()

def sum_of_proper_divisors(n):
    total = 1
    i = 2
    while i*i < n:
        if n%i == 0:
            total += i + n/i
        i += 1
    
    # Adds last divisor if n is a perfect square
    if i*i == n:
        total += i

    return total

amicable_total = 0
possible_pairs = {}

for i in range(1,10001):
    possible_pairs[i] = sum_of_proper_divisors(i)

for key,value in possible_pairs.iteritems():
    if value != key and value <= 10000 and possible_pairs[value] == key:
        amicable_total += key

end = time.clock()

print amicable_total
print "Time taken: ", end-start, " s"
