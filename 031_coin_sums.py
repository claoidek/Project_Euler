# -*- coding: utf-8 -*-

# Finds the number of different combinations of coins that can be used
# to make £2

import time

# Recursive function explores the tree of possible combinations
def add_coin(total,combinations,max_coin):
    for coin in coins:
        # Only coins <= the last coin can be added
        # This is to avoid combinations like [£1,50p,50p] and [50p,£1,50p] being
        # treated as distinct
        if coin <= max_coin:
            # Record when a new £2 combination is found
            if total+coin == 200:
                combinations += 1
            # If the total is lower than £2 the function is called again with
            # the new total
            elif total+coin < 200:
                combinations = add_coin(total+coin,combinations,coin)
    return combinations

start = time.clock()

coins = [200,100,50,20,10,5,2,1]
combinations = add_coin(0,0,200)

end = time.clock()

print combinations
print "Time taken: ", end-start, " s"
