# Finds the prime below one million that can be written as the sum of the most
# consecutive primes

import time

def is_prime(num):
    for prime in primes:
        if prime*prime>num:
            return True
        if num%prime==0:
            return False
    return True

start = time.clock()

primes = [2]
for i in range(3,1000000,2):
    if is_prime(i):
        primes.append(i)

longest_chain = 0
answer = 0

for index, start_num in enumerate(primes):
    total = start_num
    chain = 1
    i = index
    while total < 1000000 and i + 1 < len(primes):
        i += 1
        chain += 1
        total += primes[i]
        if chain > longest_chain and total in primes:
            longest_chain = chain
            answer = total

end = time.clock()

print answer
print "Time taken: ", end-start, " s"
