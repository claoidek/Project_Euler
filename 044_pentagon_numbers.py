# Finds the difference between the first pair of pentagonal numbers whose
#difference and sum are also pentagonal

import time

start = time.time()

# All pentagonal numbers found so far
pent_nums = set()

# A dictionary of all pentagonal numbers found so far that are the difference
# between two other pentagonal numbers
# They are indexed by the sum of those two numbers
pent_sums = {}

n = 0
pent = 0
found = False

while not found:
    # Generate the next pentagonal number
    pent += 3*n + 1
    pent_nums.add(pent)
    n += 1

    # Checks if current number has been used as an index yet
    # If it has then we're done and the answer is the value of that index
    if pent in pent_sums:
        diff = pent_sums[pent]
        found = True
    # If not, we check if the difference is pentagonal
    else:
        # If it is then we add if to the dictionary, indexed by the sum
        for smaller_pent in pent_nums:
            if pent - smaller_pent in pent_nums:
                pent_sums[pent + smaller_pent] = pent - smaller_pent


end = time.time()

print(diff)
print("Time taken: ", end-start, "s", sep="")
