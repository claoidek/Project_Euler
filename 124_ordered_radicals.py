# Finds the 10000th of the first 100000 numbers when sorted first by the product
# of their distinct prime factors, and then by the numbers themselves

from time import clock
import math

def prime_sieve(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# Takes in a set of lists of factors with identical length n. Computes and
# stores the product of these factors, along with the product of the distinct
# factors. While doing this, it generates and returns the set of lists of
# factors with length n+1 that have a product less than the upper limit.
def process_factors(factor_set):
    new_set = []
    for factors in factor_set:
        product = 1
        unique_prod = 1
        for prime in factors:
            product *= prime
        for prime in set(factors):
            unique_prod *= prime
        radicals[product] = unique_prod
        for prime in primes:
            if prime > factors[0]:
                break
            if prime*product <= upper_limit:
                new_set.append((prime,) + factors)
    return new_set

start = clock()

upper_limit = 100000
# Index of the term we're looking for in the final sorted list
term = 10000
primes = prime_sieve(upper_limit + 1)

# The product of the distinct prime factors of a prime is just the prime itself
radicals = {1:1}
for prime in primes:
    radicals[prime] = prime

# The maximum number of factors a number <= the upper limit can have
max_factors = int(math.log(upper_limit,2))

# Generates the set of all pairs of primes whose products are less than the
# upper limit
factor_set = []
for prime1 in primes:
    if prime1 > upper_limit/2:
        break
    for prime2 in primes:
        if prime1*prime2 > upper_limit:
            break
        else:
            factor_set.append((prime1,prime2))

# Continues generating factors until the maximum number is exceeded
for num_factors in range(2, max_factors + 1):
    factor_set = process_factors(factor_set)

# Sorts the output and locates the correct term
answer = sorted(radicals.items(), key=lambda x: (x[1],x[0]))[term-1][0]

end = clock()

print answer
print "Time taken: ", end-start, " s"
