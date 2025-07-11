# Finds the largest pandigital prime

import time
import itertools

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
            return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

start = time.time()

# The number can't be 8 or 9 digits respectively because the sum of digits would
# be 36 or 45 respectively. Both of these are multiples of 3, which makes the
# the whole number a multiple of 3.
for perm in itertools.permutations([7,6,5,4,3,2,1]):
    if is_prime(int("".join([str(x) for x in perm]))):
        break

end = time.time()

print("".join([str(x) for x in perm]))
print("Time taken: ", end-start, "s", sep="")
