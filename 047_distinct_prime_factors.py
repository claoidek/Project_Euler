# Finds the first set of four consecutive numbers that have four distinct prime
# factors, and returns the first in that sequence

import time

# Finds the number of distinct prime factors
# We cycle through primes until we find a factor
# Then the number is divided by that prime and the process is repeated
def num_prime_factors(num):
    factors = set()
    i = 0
    original = num

    while num != 1:
        # Checks if the remaining number is in the dictionary of factors 
        # If it is, we simply update the set of factors and return
        if num in dictionary:
            factors.update(dictionary[num])
            dictionary[original] = factors
            return len(factors)
        # If no factors have been found and we are past the square root of the
        # number, then the number is prime
        if primes[i]*primes[i] > num and len(factors) == 0:
            primes.append(num)
            dictionary[original] = {original}
            return 1
        if num%primes[i] == 0:
            factors.add(primes[i])
            num /= primes[i]
        # Only move to the next prime if the previous one wasn't a factor
        # This is because we need to catch factors which appear multiple times
        # in the factorisation
        else:
            i += 1

    dictionary[original] = factors
    return len(factors)

start = time.clock()

primes = [2]
# Dictionary of all numbers tested so far, and the set of their unique factors
dictionary = {2:{2}}
num_factors = 4
num_consecutive = 0
num = 2

while num_consecutive < num_factors:
    num += 1
    if num_prime_factors(num) == num_factors:
        num_consecutive += 1
    else:
        num_consecutive = 0

end = time.clock()

print num - num_factors + 1
print "Time taken: ", end-start, " s"
