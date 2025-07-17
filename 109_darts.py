# Finds the number of different ways a darts player can checkout with a score of
# less than 100.

import time
import itertools

start = time.time()

# Lists of all possible scores from a single dart
# scores[0] - singles
# scores[1] - doubles
# scores[2] - trebles
# scores[3] - misses
scores = [[],[],[],[]]
scores[0] += list(range(1,21))
scores[2] += [x * 3 for x in scores[0]]
scores[0] += [25]
scores[1] += [x * 2 for x in scores[0]]
scores[3] += [0]

checkouts = set()

for ending_double in scores[1]:
    for first_dart in range(4):
        for second_dart in range(first_dart, 4):
            for first_score in scores[first_dart]:
                for second_score in scores[second_dart]:
                    total = first_score + second_score + ending_double
                    if total < 100:
                        # We add the checkout information to a set to avoide
                        # double counting a different permutation of the same
                        # darts.
                        checkouts.add(frozenset([(first_dart,first_score),(second_dart,second_score),ending_double]))

end = time.time()

print(len(checkouts))
print("Time taken: ", end-start, "s", sep="")
