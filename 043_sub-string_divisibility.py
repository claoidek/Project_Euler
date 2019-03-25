# Finds the sum of pandigital 10-digit numbers fulfilling the following
# criteria:
# The concatenation of digits 2,3,4 is divisible by the first prime
# The concatenation of digits 3,4,5 is divisible by the second prime
# ...
# The concatenation of digits 8,9,10 is divisible by the seventh prime

import time
import itertools

def atoi(perm):
    return int("".join([str(x) for x in perm]))

start = time.clock()

total = 0
for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    # The order of some of the conditionals has been changed in order to improve
    # performance. As a rule, the most likely conditional to be filled should go
    # first.
    if perm[5] != 5:
        continue
    if sum(perm[2:5])%3 != 0:
        continue
    if perm[3]%2 != 0:
        continue
    if perm[0] == 0:
        continue
    if (perm[4]*100+perm[5]*10+perm[6])%7 !=0:
        continue
    if (perm[5]*100+perm[6]*10+perm[7])%11 !=0:
        continue
    if (perm[6]*100+perm[7]*10+perm[8])%13 !=0:
        continue
    if (perm[7]*100+perm[8]*10+perm[9])%17 !=0:
        continue
    total += atoi(perm)

end = time.clock()

print total
print "Time taken: ", end-start, " s"
