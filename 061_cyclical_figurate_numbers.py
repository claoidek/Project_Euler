# Finds a cycle of 4-digit numbers where the last two digits of each number are
# the same as the first two digits of the next.
# Additionally, one of each number must be triangle, square, pentagonal,
# hexagonal, heptagonal, and octagonal.

import time
import itertools

# Finds all 4-digit numbers from each of the six categories
def generate_numbers(index):
    n = 1
    num = 1
    while num < 10000:
        num = int(n*coefficients[index][0]* \
                (n*coefficients[index][1] + coefficients[index][2]))
        n += 1
        if num >= 1000 and num < 10000:
            allnums[index].append(str(num))

# Recursive function to find valid chains of numbers
# Tests all numbers from the category specified by the index
# If they match, two non-overlapping digits are added on, and the function is
# called again with the next index
# If any root does not have a valid chain associated with it, None is returned
# back down the chain of recursion
def match_ends(root, index):
    for num in allnums[perm[index]]:
        if root[-2:] == num[:2]:
            if index == 4:
                return root + num[2:]
            match = match_ends(root + num[2:], index + 1)
            return match
    return None

start = time.time()

# Stores all the different categories of numbers
allnums = [[],[],[],[],[],[]]

# Coefficients for generating the numbers
# For example, the formula for generating triangular numbers is 0.5*n*(n + 1)
coefficients = [[0.5,  1,  1], \
                [  1,  1,  0], \
                [0.5,  3, -1], \
                [  1,  2, -1], \
                [0.5,  5, -3], \
                [  1,  3, -2]]

for i in range(6):
    generate_numbers(i)

found = False

# Iterates over all possible orderings of the categories
# We always start with triangular numbers, as it doesn't matter where the cycle
# begins
for perm in itertools.permutations([1,2,3,4,5]):
    for num in allnums[0]:
        match = match_ends(num, 0)
        # If a chain is valid, we check if it's also a cycle
        if match is not None and match[:2] == match[-2:]:
            total = 0
            # Extract the sum of the individual numbers from the cycle
            for i in range(6):
                total += int(match[i*2:i*2+4])
            # We're told that there is only one solution so we can break after
            # finding one
            found = True
            break
    if found:
        break

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
