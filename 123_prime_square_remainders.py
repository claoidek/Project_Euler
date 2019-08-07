# Finds the least n such that ((p-1)^n+(p+1)^n) mod p^2 > 10^10
# where p is the nth prime

# This problem uses identical logic to problem 120

from time import clock

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

start = clock()

remainder = 10**10
primes = []
prime_sieve(1000000)

# It can be seen by expanding (p-1)^n+(p+1)^n that the last term in the
# expansion is 2 for even n and 2pn for odd n. All other terms have order >=2
# so they are equal to 0 mod p^2. Hence, we only need to consider the
# contribution of the last term.
# This means we can iterate through all odd n until we find one which gives
# 2pn>10*10
for index, prime in enumerate(primes[0::2]):
    if 2*prime*(2*index+1) > remainder:
        break

end = clock()

print 2*index+1
print "Time taken: ", end-start, " s"
