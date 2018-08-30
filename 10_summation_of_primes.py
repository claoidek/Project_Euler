# Finds the sum of all primes below 2 million

import time

def is_prime(num):
    for prime in primes:
        if prime*prime>num:
            return True
        if num%prime==0:
            return False
    return True

start = time.clock()

upper_bound = 2000000
primes = [2]
total = 2
num = 3

while num < upper_bound:
    if is_prime(num):
        primes.append(num)
        total += num
    num += 2

end = time.clock()

print total
print "Time taken: ", end-start, " s"
