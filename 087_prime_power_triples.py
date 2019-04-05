# Finds all numbers under fifty million that can be written as the sum of a
# prime square, prime cube, and prime fourth power

import time

def prime_sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p*p <= n: 
        if prime[p] == True:
            for i in range(p*2,n + 1,p):
                prime[i] = False
        p += 1
    for p in range(2,n):
        if prime[p]:
            primes.append(p)

start = time.clock()

primes = []
prime_sieve(7071)

prime_squares = []
prime_cubes = []
prime_fourths = []

for prime in primes:
    prime_squares.append(prime**2)
    if prime <= 368:
        prime_cubes.append(prime**3)
    if prime <= 84:
        prime_fourths.append(prime**4)

found = set()

for prime_square in prime_squares:
    for prime_cube in prime_cubes:
        for prime_fourth in prime_fourths:
            if prime_square + prime_cube + prime_fourth < 50000000:
                found.add(prime_square + prime_cube + prime_fourth)
            else:
                break

end = time.clock()

print len(found)
print "Time taken: ", end-start, " s"
