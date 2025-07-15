# Computes the number of pairs of disjoint subsets of equal length that need to
# be tested for equality to ensure that no such pairs of subsets have equal
# sums.

import time
import itertools
import math

start = time.time()

# The problem wants us to find the answer for a set of size 12. We use range()
# in order to ensure that the set is sorted and to allow us to use the elements
# directly instead of their indices.
test_set = range(12)
count = 0

for length in range(2, len(test_set)//2 + 1):
    for subset_a in itertools.combinations(test_set,length):
        for subset_b in itertools.combinations \
                (set(test_set).difference(subset_a),length):
                    sign = 0
                    # We compare the lowest element in each subset, and then the
                    # second lowest etc. If the larger element in every pair is
                    # from the same subset then the subsets do not need to be
                    # tested for equality as one is strictly larger than the
                    # other regardless of the values used. We count all the
                    # subset pairs for which this is not true in order to get
                    # our answer.
                    for i in range(length):
                        sign += math.copysign(1, subset_a[i] - subset_b[i])
                    if (abs(sign) != length):
                        count += 1

end = time.time()

print(count//2)
print("Time taken: ", end-start, "s", sep="")
