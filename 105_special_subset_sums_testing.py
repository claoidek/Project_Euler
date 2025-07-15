# Finds all special sum sets in external_files/105_sets.txt and computes the sum
# of all elements in those sets
# Special sum sets are defined here: https://projecteuler.net/problem=105

import time
import math
import itertools
import csv

def is_special(test_set):
    # Make sure there are no repeated elements
    if len(test_set) != len(set(test_set)):
        return False

    # Check if B containing more elements than C implies S(B)>S(C)
    upper_mid = int(math.ceil(len(test_set)/2.))
    lower_mid = len(test_set)//2
    for i in range(2,upper_mid + 1):
        if sum(test_set[:i]) <= sum(test_set[-(i-1):]):
            return False

    # Make sure there are no disjoint non-empty subsets with equal sums
    # This method of checking isn't optimal, but it is good enough
    for length in range(2,lower_mid + 1):
        for subset_a in itertools.combinations(test_set,length):
            for subset_b in itertools.combinations \
                    (set(test_set).difference(subset_a),length):
                if sum(subset_a) == sum(subset_b):
                    return False

    return True
    
    
start = time.time()

total = 0
test_sets = []

with open("external_files/105_sets.txt") as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        test_sets.append(sorted([int(x) for x in line]))


for test_set in test_sets:
    if(is_special(test_set)):
        total += sum(test_set)

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
