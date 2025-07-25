# Finds the sum of all numbers that can be written as the sum of fifth powers of
# their digits.

import time

def sum_of_fifth_powers(n):
    return sum([int(i)**5 for i in str(n)])

start = time.time()

# No need to check any numbers above this limit because the sum of fifth powers
# of higher numbers will not be the correct number of digits, even if all digits
# are 9's.
theoretical_max = 6*9**5

total = sum([i for i in range(2,theoretical_max+1) if i == sum_of_fifth_powers(i)])

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
