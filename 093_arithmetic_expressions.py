# Finds the set of 4 digits that can be combined to make the longest string of
# consecutive integers starting from 1
# Each digit must be used exactly once
# The operators +,-,*,/ are allowed

import time
import itertools

# Performs the specified operation on a and b
def calc(a,b,op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a*b
    if op == 3:
        if b != 0:
            return float(a)/b
        else:
            # Since we're searching for integers, we just return a random float
            # to ensure the total won't be an integer
            # This avoids having to set up a special way of handling zero
            # division
            return a + 0.123456

start = time.time()

longest = 0

# Loop over all sets of 4 unique digits
for digits in itertools.combinations(range(1,10),4):
    solutions = set()
    # Loop over all digit orders
    for a,b,c,d in itertools.permutations(digits):
        # Loop over all combinations of operations
        for operations in itertools.product(range(4),repeat = 3):
            # The two options are:
            # (((a ~ b) ~ c) ~ d)
            # ((a ~ b) ~ (c ~ d))
            # Everything else will be covered by either changing the order of
            # operations or order of digits
            answers = []
            a_op_b = calc(a,b,operations[0])
            answers.append(calc(calc(a_op_b,c,operations[1]),d,operations[2]))
            answers.append(calc(a_op_b,calc(c,d,operations[1]),operations[2]))
            for answer in answers:
                if float(answer).is_integer() and answer > 0:
                    solutions.add(int(answer))
    
    # Check if longest sequence has been improved on
    for index,item in enumerate(sorted(list(solutions))):
        if index != item - 1:
            if index > longest:
                longest = index
                solution = "".join([str(x) for x in digits])
            break

end = time.time()

print(solution)
print("Time taken: ", end-start, "s", sep="")
