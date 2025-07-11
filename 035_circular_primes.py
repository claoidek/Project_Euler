# Finds the number of primes below one million for which all rotations are also
# primes.
# For example: 197, 971, and 719 are all prime.

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

# Returns a list of tuples representing all possible rotations of the input
# tuple
def number_cycles(number):
    cycles = [number]
    for i in range(len(number) - 1):
        cycles.append(tuple(cycles[-1][1:] + cycles[-1][0:1]))
    return cycles

# Returns True if all of the numbers represented by the list of input tuples are
# prime, and False otherwise
def check_cycles(cycles):
    for cycle in cycles:
        if not is_prime(int("".join([str(x) for x in cycle]))):
            return False

    return True

start = time.time()

candidates = set()
circ_primes = {2,3,5,7}
rejected = set()

# Finds all candidate numbers by creating a set of all numbers <1000000 composed
# only of the digits 1,3,7,9. Any number that contains any other digit will have
# at least one rotation that is divisible by either 2 or 5.
for num_digits in range(2,7):
    for comb in itertools.combinations_with_replacement([1,3,7,9],num_digits):
        for perm in itertools.permutations(comb):
            candidates.add(perm)

for number in candidates:
    if number in circ_primes or number in rejected:
        continue
    cycles = number_cycles(number)
    if check_cycles(cycles):
        for cycle in cycles:
            circ_primes.add(cycle)
    else:
        for cycle in cycles:
            rejected.add(cycle)

end = time.time()

print(len(circ_primes))
print("Time taken: ", end-start, "s", sep="")
