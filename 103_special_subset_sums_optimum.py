# Finds the optimum special sum set for n = 7
# Special sum sets are defined here: https://projecteuler.net/problem=103

import time
import math
import itertools

# Method for finding a near optimum special sum set from the optimum special sum
# set for the preceding n
def near_optimum_set(previous_set):
    middle = previous_set[len(previous_set)//2]
    output = [middle]
    for entry in previous_set:
        output.append(entry + middle)
    return output

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

# The optimum special sum set for n = 6
optimum_six = [11,18,19,20,22,25]
initial_guess = near_optimum_set(optimum_six)
min_sum = sum(initial_guess)
best_set = initial_guess

# We assume that since we're near the optimum that each term will be within 3 of
# the optimum
for delta in itertools.product(range(-3,4),repeat=len(initial_guess)):
    if sum(delta) >= 0:
        continue
    test_set = initial_guess[:]
    for i in range(len(test_set)):
        test_set[i] += delta[i]
    if sum(test_set) < min_sum and is_special(sorted(test_set)):
        min_sum = sum(test_set)
        best_set = test_set

end = time.time()

print("".join([str(x) for x in best_set]))
print("Time taken: ", end-start, "s", sep="")
