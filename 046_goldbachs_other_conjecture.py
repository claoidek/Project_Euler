# Finds the first odd composite number that cannot be written as the sum of a
# prime and twice a square.

import time

def is_prime(num):
    for prime in primes:
        if prime*prime>num:
            primes.append(num)
            return True
        if num%prime==0:
            return False
    return True

start = time.time()

primes = [2,3,5,7]

num = 7
found = False

while not found:
    num += 2
    if is_prime(num):
        continue
    base = 1
    while 2*base*base < num:
        if num - 2*base*base in primes:
            break
        base += 1
    if 2*base*base > num:
        found = True


end = time.time()

print(num)
print("Time taken: ", end-start, "s", sep="")
