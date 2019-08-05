# Finds the smallest n for which the equation 1/x + 1/y = 1/n has more than 1000
# solutions

# For the equation to hold, we must have x,y > n, so we can rewrite as:
# 1/(n+a) + 1/(n+b) = 1/n
# Which after rearranging and simplifying gives:
# n^2 = ab
# So the answer will be the smallest n^2 that has over 1000 pairs of factors a,b

# We can reduce the the search space by noting that if n has a pair of factors
# c,d then cn,d and c,dn will both be factors of n^2
# This means that for every two divisors of n, we can generate four divisors of
# n^2
# The only exception to this is the pair 1,n which generates the two pairs 1,n^2
# and n,n which only add three divisors of n^2
# Therefore, if n has p divisors, n^2 has 2p - 1

# Finally, we have that the number of divisors of a number n with prime
# factorisation (p1^a1)*(p2^a2)*...*(pk^ak) is given by:
# (a1 + 1)*(a2 + 1)*...*(ak + 1)
# This is shown in Equation 3 here:
# http://mathworld.wolfram.com/DivisorFunction.html
# This means that the number of divisors of n^n is: 
# (2*a1 + 1)*(2*a2 + 1)*...*(2*ak + 1)

from time import clock

def prime_factors(num):
    factors = []
    i = 0
    original = num

    while num != 1:
        if num in dictionary:
            factors += dictionary[num]
            dictionary[original] = factors
            return factors
        if primes[i]*primes[i] > num and len(factors) == 0:
            primes.append(num)
            dictionary[original] = {original}
            return [original]
        if num%primes[i] == 0:
            factors.append(primes[i])
            num /= primes[i]
        else:
            i += 1

    dictionary[original] = factors
    return factors

start = clock()


primes = [2,3]
# Dictionary of all numbers tested so far, and the list of their unique factors
dictionary = {2:[2],3:[3]}

num_divisors = 0
n = 3

# For the number of factor pairs to be > 1000, the number of divisors must be 
# > 1999
while num_divisors <= 1999:
    n += 1
    factors = prime_factors(n)
    num_divisors = 1
    for prime in set(factors):
        num_divisors *= 2*factors.count(prime) + 1

end = clock()

print n
print "Time taken: ", end-start, " s"
