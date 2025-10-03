# For each digit 0-9, finds the set of 10-digit primes that have the maximum
# number of that digit. The sum of every element in all 10 sets is then
# calculated.

import time
import itertools

def prime_sieve(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

start = time.time()

total = 0
num_digits = 10

primes = prime_sieve(int((10**num_digits)**0.5))

for digit in range(10):
    prime_found = False
    # We begin testing with the number that contains only the digit of interest
    # (e.g. 1111111111) and then iterate downwards. This means we don't need to
    # investigate every prime, as once we have found one with a certain number
    # of matching digits we no longer care about any with a smaller number.
    for num_copies in range(num_digits,0,-1):
        candidates = set()
        # Special case for number with all digits matching.
        if num_copies == num_digits:
            if digit == 1:
                candidates.add(int("".join(map(str,[digit]*num_digits))))
            else:
                # Only numbers with all 1s can be prime as any other digit will
                # be a multiple of that one.
                continue
        # If the number of matching digits is less than the total number of
        # digits then we generate all possible combinations of digits that could
        # fill in the rest.
        for other_digits in itertools.product(range(10), repeat = num_digits - num_copies):
            # We generate all possible positions that the non-matching digits
            # could take in the number.
            for positions in itertools.combinations(range(num_digits), num_digits - num_copies):
                # Construct the number using the process described above and add
                # it to a set to be tested for primality later.
                candidate = [digit]*num_digits
                for other_digit_index in range(num_digits - num_copies):
                    candidate[positions[other_digit_index]] = other_digits[other_digit_index]
                    candidate_num = int("".join(map(str,candidate)))
                    # Check to not add any numbers with leading 0s.
                    if candidate_num > 10**(num_digits-1):
                        candidates.add(candidate_num)
        # Check all numbers in our testing set for primality, and add them to
        # the total if they are.
        for candidate in candidates:
            is_prime = True
            for prime in primes:
                if candidate%prime == 0:
                    is_prime = False
                    break
            if is_prime:
                total += candidate
                prime_found = True
        # If we have found a prime we no longer need to test numbers with a
        # lower number of matching digits.
        if prime_found:
            break

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
