# Finds the smallest member of a family of 8 primes that differ only by
# replacing certain parts of the number with the same digit.
# For example, the smallest family of 7 primes is (56003, 56113, 56333, 56443,
# 56663, 56773, 56993)

from time import clock

def is_prime(num):
    if num == 1:
        return False
    for prime in primes:
        if prime*prime>num:
            return True
        if num%prime==0:
            return False
    return True

# Returns all primes with the specified number of digits, as well as appending
# them to the global set of primes
def generate_primes(num_digits):
    n_digit_primes = []
    for i in range(10**(num_digits - 1) + 1, 10**num_digits,2):
        if is_prime(i):
            primes.append(i)
            n_digit_primes.append(i)
    return n_digit_primes

start = clock()

primes = [2,3,5,7]

# Generate all primes up to 4 digits in order because these will be needed to
# generate primes with 5+ digits
for i in range(2,5):
    n_digit_primes = generate_primes(i)

found = False

# We are told that the smallest family of 7 primes have 5 digits, so we don't
# need to check primes with 4 digits or fewer
num_digits = 5

num_required = 8
smallest_of_set = []

# This loop finds all candidate numbers for the current number of digits
# If there are none, we increase the number of digits and continue
# If there are multiple candidates we need to find the smallest one afterwards
# We can't stop at the first one we find, because the numbers will not
# necessarily be found in order of size
while not found:
    # This dictionary is indexed by primes with their repeated digits left blank
    # The values are the number of times each pattern was found
    pattern_count = {}
    n_digit_primes = generate_primes(num_digits)

    for prime in n_digit_primes:
        str_prime = str(prime)

        for digit in set(str_prime):
            count = str_prime.count(digit)
            # The digit must be appear at least 3 times
            # If it only appears twice then at least 3 of the numbers produced
            # will have a digital sum that is a multiple of 3
            # This means the numbers themselves would also be multiples of 3
            # and we would not have enough to make 8 primes.
            if count >= 3:
                # 56003 -> ("5","6",None,None,"3")
                pattern = tuple([x if x != digit else None for x in str_prime])
                if pattern in pattern_count:
                    pattern_count[pattern] += 1
                else:
                    pattern_count[pattern] = 1

    for pattern in pattern_count:
        # This is the number of times the pattern must have appeared in order
        # for it to be possible to have 8 primes in the family
        # Note that the number is not simply num_required, as it excludes primes
        # that do not replace ALL instances of a digit
        # For example, in the 7 prime family above: 56003, 56113, 56443, 56773, 
        # and 56993 all map to (5,6,None,None,3), but 56333 and 56663 map to
        # (5,6,None,None,None) and (5,None,None,None,3) respectively
        if pattern_count[pattern] < \
                num_required - num_digits + pattern.count(None):
            continue

        num_primes = 0
        num_non_primes = 0

        # We iterate backwards for convenience in order to end up with the
        # smallest prime at the end
        for i in range(9,-1,-1):
            # Break if we no longer can reach 8 primes
            if num_non_primes > 10 - num_required:
                break
            # Taking care of leading zeroes
            if pattern[0] is None and i == 0:
                num_non_primes += 1
                continue
            num = int("".join([x if x is not None else str(i) for x in pattern]))
            if num in primes:
                num_primes += 1
                prime = num
            else:
                num_non_primes += 1

        if num_primes == num_required:
            smallest_of_set.append(prime)
            # Flag that a family have been found so we don't need to go to the
            # next number of digits up
            found = True

    num_digits += 1

end = clock()

print min(smallest_of_set)
print "Time taken: ", end-start, " s"
