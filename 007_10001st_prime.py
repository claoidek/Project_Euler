# Finds the 10001st prime

import time

def is_prime(num):
    for prime in primes:
        if prime*prime > num:
            return True
        if num%prime == 0:
            return False
    return True

start = time.clock()

n = 10001
primes_found = 1
primes = [2]
candidate_prime = 1

while primes_found < n:
    candidate_prime += 2
    if is_prime(candidate_prime):
        primes.append(candidate_prime)
        primes_found += 1

end = time.clock()

print candidate_prime
print "Time taken: ", end-start, " s"
