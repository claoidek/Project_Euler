# There are two sequences of three four-digit numbers that fulfil the following
# three criteria:
# All three are permutations of each other
# All three are prime
# The middle number is exactly halfway between the other two
#
# One of the sequences is 1487,4817,8147
# This program finds the other

import time
import itertools

def is_prime(num):
    for prime in primes:
        if prime*prime>num:
            return True
        if num%prime==0:
            return False
    return True

start = time.time()

# Create a list of all primes with four digits or less
primes = [2]
for i in range(3,10000,2):
    if is_prime(i):
        primes.append(i)

# Only primes with four digits
four_digits = [x for x in primes if x>999]

# Dictionary of sets of numbers, indexed by their digits in increasing order
anagram_dict = {}

for num in four_digits:
    key = tuple(sorted([int(x) for x in str(num)]))
    if key in anagram_dict:
        anagram_dict[key].add(num)
    else:
        anagram_dict[key] = {num}

# Checks the sets for three numbers that fulfill the criteria
for key in anagram_dict:
    if len(anagram_dict[key]) > 3:
        for a,b in itertools.combinations(sorted(anagram_dict[key]),2):
            if 2*b - a in anagram_dict[key] and a != 1487:
                print(str(a) + str(b) + str(2*b - a))

end = time.time()

print("Time taken: ", end-start, "s", sep="")
