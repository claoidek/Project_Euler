# Finds the n <= 10000000 for which n/phi(n) is minimised and phi(n) is a
# permutation of n
# Phi is Euler's Totient function, which is defined here:
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# In order to minimise n/phi(n) we need to maximise phi(n)
# For this to be true we need n to be relatively prime to as many numbers as
# possible
# This means minimising the number of prime factors of n
# n cannot be prime because then phi(n) would be n-1, and n-1 cannot be a
# permutation of n
# This means that n will be a product of two primes
# These primes should both be as large as possible, to maximise the amount of
# numbers n is relatively prime to
# For this reason, we begin our searching at sqrt(10000000)

from time import clock
import itertools
import math

def prime_sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n: 
        if prime[p] == True:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2,n):
        if prime[p]:
            primes.append(p)

start = clock()

primes = []
prime_sieve(5000)

minimum = 9999.0
min_diff = 9999
min_n = 0

# Finds the index of the first prime > sqrt(100000000)
pivot = primes.index(next(x for x in primes if x > math.sqrt(10000000)))

# Check primes in both directions from the pivot
for a in primes[pivot-1::-1]:
    for b in primes[pivot:]:
        n = a*b
        if n > 10000000:
            break
        # We want to maximise n and minimise the difference between the two
        # primes
        # If the current pair are worse on both counts then we need not check
        # them further
        if n < min_n and b - a > min_diff:
            continue
        tot = (a-1)*(b-1)
        if sorted(str(n)) == sorted(str(tot)):
            if minimum > float(n)/tot:
                minimum = float(n)/tot
                min_n = n
                min_diff = b - a

end = clock()

print min_n
print "Time taken: ", end-start, " s"
