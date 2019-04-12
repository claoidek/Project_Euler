# Finds the number of combinations of digits that can be placed on two six-sided
# dice such that all square numbers under 100 can be displayed
# Note that 6 can be used for either 6 or 9 and vice versa

from time import clock
import itertools

def check_validity(d1,d2):
    # Check sides are distinct
    if len(set(d2)) < len(d2):
        return False
    # 01
    if not (((0 in d1) and (1 in d2)) or ((1 in d1) and (0 in d2))):
        return False
    # 04
    if not (((0 in d1) and (4 in d2)) or ((4 in d1) and (0 in d2))):
        return False
    # 09
    if not (((0 in d1) and (6 in d2 or 9 in d2)) or ((6 in d1 or 9 in d1) and (0 in d2))):
        return False
    # 16
    if not (((1 in d1) and (6 in d2 or 9 in d2)) or ((6 in d1 or 9 in d1) and (1 in d2))):
        return False
    # 25
    if not (((2 in d1) and (5 in d2)) or ((5 in d1) and (2 in d2))):
        return False
    # 36
    if not (((3 in d1) and (6 in d2 or 9 in d2)) or ((6 in d1 or 9 in d1) and (3 in d2))):
        return False
    # 49 and 64
    if not (((4 in d1) and (6 in d2 or 9 in d2)) or ((6 in d1 or 9 in d1) and (4 in d2))):
        return False
    # 81
    if not (((1 in d1) and (8 in d2)) or ((8 in d1) and (1 in d2))):
        return False
    return True

start = clock()

valid = 0

# The dice must contain at least one of each of these numbers
required = [0,1,2,3,4,5,8]

pool = [0,1,2,3,4,5,6,7,8,9]

# Pick a random set of six numbers
for comb in itertools.combinations(pool,6):
    d1 = list(comb)
    essential = []
    remaining = 6
    # Make sure d2 has all the remaining required numbers
    for num in required:
        if num not in d1:
            essential.append(num)
            remaining -= 1
    # Fill out the remaining spots in d2 with the some combination of the
    # remaining numbers
    unused = list(set(pool).difference(set(essential)))
    for remainder in itertools.combinations(unused,remaining):
        d2 = list(essential)
        d2.extend(remainder)
        if check_validity(d1,d2):
            valid += 1

end = clock()

# This method counts each combination twice because it differentiates between
# the two dice, so we must divide by two
print valid/2
print "Time taken: ", end-start, " s"
