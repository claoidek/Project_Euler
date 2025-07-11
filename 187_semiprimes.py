# Finds the number of integers < 10^8 that have exactly two prime factors

import time

def prime_sieve(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

start = time.time()

limit = 10**8

primes = prime_sieve(limit//2)

total = 0

for prime1 in primes:
    for prime2 in primes:
        if prime2 > prime1 or prime1*prime2 >= limit:
            break
        total += 1


end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
