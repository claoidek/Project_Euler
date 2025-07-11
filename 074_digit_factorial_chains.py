# Takes each number under a million and forms a chain where each term is equal
# to the sum of the factorials of the preceding terms digits
# This is done until a term would be repeated
# This program finds all such chains that have a length of 60

import time

def factorial_sum(num):
    total = 0
    for digit in str(num):
        total += factorials[int(digit)]
    return total

def chain_length(num,prev):
    # We use the sorted digits as the key, because the order of the digits
    # doesn't matter for the sum of factorials
    digits = tuple(sorted(str(num)))
    if digits in master:
        return master[digits]

    next_term = factorial_sum(num)
    # End of chain
    if next_term in prev:
        return 1

    # If we haven't found the length, call recursively with the next number in
    # the chain
    prev.append(next_term)
    length = chain_length(next_term,prev) + 1
    # We only record lengths of 4 or greater
    # This is because the last three numbers may be part of the loop
    # 3 is the cutoff because we are told that there are no loops with length>3
    if length > 3:
        master[digits] = length
    return length

start = time.time()

# Stores the chain length for each combination of digits
master = {}

# Precomputed factorials to save time
factorials = [1,1,2,6,24,120,720,5040,40320,362880]

sixties = 0
for i in range(1000000):
    if chain_length(i,[i]) == 60:
        sixties += 1

end = time.time()

print(sixties)
print("Time taken: ", end-start, "s", sep="")
