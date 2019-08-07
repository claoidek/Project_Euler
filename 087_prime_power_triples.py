# Finds all numbers under fifty million that can be written as the sum of a
# prime square, prime cube, and prime fourth power

from time import clock

def prime_sieve(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

start = clock()

primes = prime_sieve(7071)

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

end = clock()

print len(found)
print "Time taken: ", end-start, " s"
