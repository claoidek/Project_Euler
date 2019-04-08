# A number chain is created by recursively taking the sum of the square of the
# digits of the previous number
# This program finds all starting numbers under ten million whose chains
# terminate in a loop containing the number 89

import time
from itertools import combinations_with_replacement
from collections import Counter
from math import factorial

def square_and_add(num):
    total = 0
    for digit in num:
        total += digit*digit
    return total

# For a list of digits, finds the number of unique permutations of those digits
# Uses the formula found here:
# https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets
def permutations(comb):
    total = 1
    for i in Counter(comb).values():
        total *= factorial(i)
    return factorial(len(comb))/total

start = time.clock()

total = 0
# All chains starting with a positive integer end in either 1 or 89
chain_ends = {0:0,1:1,89:89}
limit = 10**7
# The maximum amount of digits a starting number can have
max_digits = len(str(limit)) - 1

# Creates a lookup for the values <= max_digits*9^2
# This upper limit is the maximum value a term can have after the first
# iteration of the chain
# 9999999 -> 7*9^2 = 567
for i in range(1,max_digits*81 + 1):
    if i in chain_ends:
        continue
    num = i
    chain = [num]
    while num not in chain_ends:
        chain.append(num)        
        num = square_and_add([int(x) for x in str(num)])
    for link in chain:
        chain_ends[link] = chain_ends[num]

# Since the next value in the chain is independent of the order of the digits of
# the preceding value, we only need to loop over all combinations of digits
# We then calculate the number of unique permutations of those combinations to
# work out how many numbers terminate at 89
for comb in combinations_with_replacement(range(10),max_digits):
    if chain_ends[square_and_add(comb)] == 89:
        total += permutations(comb)

end = time.clock()

print total
print "Time taken: ", end-start, " s"
