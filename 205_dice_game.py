# Finds the probability of rolling a higher total on 9 pyramidal (4-sided) dice,
# than on 6 cubic (6-sided) dice

from __future__ import division
from time import clock
import itertools

start = clock()

p_totals = {}
num_p_perms = 0
c_totals = {}
num_c_perms = 0
prob = 0.0

# Computes the distribution of totals for the pyramidal dice
for comb in itertools.product(range(1,5), repeat = 9):
    total = sum(comb)
    num_p_perms += 1
    if total in p_totals:
        p_totals[total] += 1
    else:
        p_totals[total] = 1

# Computes the distribution of totals for the cubic dice
for comb in itertools.product(range(1,7), repeat = 6):
    num_c_perms += 1
    total = sum(comb)
    if total in c_totals:
        c_totals[total] += 1
    else:
        c_totals[total] = 1

# For each possible total on the cubic dice, compute the probability of rolling
# higher on the pyramidal dice
for c_total in c_totals:
    higher = 0
    for p_total in p_totals:
        if p_total > c_total:
            higher += p_totals[p_total]
    prob += (c_totals[c_total]*higher)/(num_p_perms*num_c_perms)

end = clock()

# Print to 7 decimal places
print '%.7f' % prob
print "Time taken: ", end-start, " s"
