# Finds the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime
# This is very slow. The majority of time is spent finding the pairs of primes
# that concatenate to form other primes. Everything else runs in less than a
# second.
from time import clock
import itertools

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

def is_prime(num):
    if num in primes:
        return True
    for prime in primes:
        if prime*prime > num:
            return True
        if num%prime == 0:
            return False

    i = primes[-1] + 2
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

def sum_of_digits(num):
    return sum([int(x) for x in str(num)])

start = clock()

primes = []
primes_0 = [3]
primes_1 = [3]
primes_2 = [2,3]


# This figure needs to be bigger than the largest prime in the final answer,
# but otherwise the smaller the better
# It's set to the optimal value here as it significantly improves the runtime
prime_sieve(8390)

prime_pairs = {3:set()}
prime_triplets = {}
prime_quartets = {}
prime_quintets = []

# Divides all the primes in groups based on the sum of their digits mod 3
# This is to reduce the number of other primes they need to be compared with, as
# the sum of the digits in the concatenated number cannot be a multiple of 3
# without being non-prime
for prime in primes[2:]:
    case = sum_of_digits(prime)%3
    if case == 1:
        primes_1.append(prime)
    else:
        primes_2.append(prime)

# Finds all pairs of primes that can be concatenated either way to form two
# other primes
# A dictionary is created where each prime indexes the set of all bigger valid
# primes
# >99% of the runtime is spent in the next three loops

# Special case for 3
for b in primes_1 + primes_2:
    if is_prime(int("3" + str(b))) and is_prime(int(str(b) + "3")):
        prime_pairs[3].add(b)

# Sum of digits mod 3 = 1
for a,b in itertools.combinations(primes_1,2):
    if is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))):
        if a in prime_pairs:
            prime_pairs[a].add(b)
        else:
            prime_pairs[a] = {b}

# Sum of digits mod 3 = 2
for a,b in itertools.combinations(primes_2,2):
    if is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))):
        if a in prime_pairs:
            prime_pairs[a].add(b)
        else:
            prime_pairs[a] = {b}

# Finds intersections between the sets in prime_pairs to get all valid triplets
for a in prime_pairs:
    for b in prime_pairs[a]:
        # Each pair must share at least three common partners in order for it to
        # be possible for them to be part of a quintuplet
        if b in prime_pairs and len(prime_pairs[a].intersection(prime_pairs[b])) >= 3:
            prime_triplets[(a,b)] = prime_pairs[a].intersection(prime_pairs[b])

# Same again for quartets
for a,b in prime_triplets:
    for c in prime_triplets[(a,b)]:
        if c in prime_pairs and len(prime_triplets[a,b].intersection(prime_pairs[c])) >= 2:
            prime_quartets[(a,b,c)] = prime_triplets[a,b].intersection(prime_pairs[c])

# And lastly for quintets
for a,b,c in prime_quartets:
    for d in prime_quartets[(a,b,c)]:
        if d in prime_pairs and len(prime_quartets[a,b,c].intersection(prime_pairs[d])) > 0:
            for e in prime_quartets[a,b,c].intersection(prime_pairs[d]):
                prime_quintets.append((a,b,c,d,e))

min_sum = 99999999999999999
for quintet in prime_quintets:
    if sum(quintet) < min_sum:
        min_sum = sum(quintet)
end = clock()

print min_sum
print "Time taken: ", end-start, " s"
