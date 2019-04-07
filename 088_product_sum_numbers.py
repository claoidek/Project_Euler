# Finds the sum of all the minimal product-sum numbers of set size k for
# 2<=k<=12000
# More information on product-sum numbers can be found here:
# https://projecteuler.net/problem=88

import time
import math

def set_product(set_in):
    total = 1
    for i in set_in:
        total *= i
    return total

start = time.clock()

max_k = 12000
# For any k, 2k is a product-sum number with a set of 2, k and (k - 2) 1's
# Since we're looking for a minimum we don't need to check any numbers above
# this
limit = max_k*2
# The maximum number of factors a number can have whilst still being <= 2k
max_factors = int(math.log(limit,2))

# Minimal product-sum number found so far for each k
min_found = [limit for x in range(2,max_k + 1)]

# Sets of factors that have a product <= max_k*2, grouped by number of factors
factors = [set() for x in range(max_factors - 1)]

# Generates all valid sets of 2 factors
for a in range(2,max_k + 1):
    for b in range(2,a + 1):
        if a*b >= limit:
            break
        factors[0].add((b,a))
        # Since we can add an arbitrary number of 1's to the set without
        # changing the product, the difference between the product and the sum
        # of the factors is the number of 1's that must be added to make it a
        # product-sum number
        # We then add 2 (the original number of factors) to get the length of
        # the set (k)
        set_length = a*b - (a + b) + 2
        # Check if this number is the minimal product-sum for k
        if set_length <= max_k and a*b < min_found[set_length - 2]:
             min_found[set_length - 2] = a*b

# Generates all valid sets of factors by appending numbers to the existing sets
for num_factors in range(3,max_factors + 1):
    for factor_set in factors[num_factors - 3]:
        product = set_product(factor_set)
        # We only need to add numbers that are <= the smallest number in the
        # existing set
        # Checking higher numbers would be a waste as they will be found as
        # part of a different set
        # For example, if the existing set is [2,5], we don't need to add [3],
        # as we will find the set [2,3,5] later by adding [2] to [3,5]
        for i in range(2,factor_set[0] + 1):
            if i*product >= limit:
                break
            # We don't need to save the sets with the maximum number of factors
            if num_factors != max_factors:
                factors[num_factors - 2].add((i,) + factor_set)
            # Find set length and check if minimal the same way we did for 2
            # factors
            set_length = i*product - sum(factor_set) + num_factors - i
            if set_length <= max_k and i*product < min_found[set_length - 2]:
                 min_found[set_length - 2] = i*product

end = time.clock()

print sum(set(min_found))
print "Time taken: ", end-start, " s"
