# Finds the first number that can be written as a sum of primes over 5000
# different ways

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

# Sum of the distinct primes dividing n
def prime_sum(n):
    if n in sums:
        return sums[n]
    total = 0
    if n in primes:
        total = n
    for prime in primes:
        if prime*2 > n:
            break
        if n%prime == 0:
            total += prime
    sums[n] = total
    return total

# Number of prime partitions of n
# Uses the formula described here: https://oeis.org/A000607
def partition(n):
    if n in partitions:
        return partitions[n]
    total = 0
    for k in range(1,n + 1):
        total += prime_sum(k)*partition(n - k)
    total /= n
    partitions[n] = total
    return total

start = clock()

partitions = {0:1}
sums = {1:0}

# The number of prime partitions grows extremely quickly, so we don't need many
# primes
primes = []
prime_sieve(100)

i = 2
while partition(i) <= 5000:
    i += 1

end = clock()

print i
print "Time taken: ", end-start, " s"
