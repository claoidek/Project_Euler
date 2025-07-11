# Finds the millionth lexicographic permutation of the digits 0123456789

import time
import itertools

start = time.time()

digits = [0,1,2,3,4,5,6,7,8,9]

permutation_count = 0

for permutation in itertools.permutations(digits,10):
    permutation_count += 1
    if permutation_count == 1000000:
        break

end = time.time()

print("".join(str(x) for x in permutation))
print("Time taken: ", end-start, "s", sep="")
