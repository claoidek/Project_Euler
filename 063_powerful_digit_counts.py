# Finds all the n-digit positive integers that are also an nth power

import time

start = time.clock()

total = 0
i = 1

# If 9^i isn't long enough, then there are no more valid solutions for greater i
while len(str(9**i)) >= i:
    # 10^i has i+1 digits, so we only need to check up to 9
    for j in range(1,10):
        if len(str(j**i)) == i:
            total += 1
    i += 1

end = time.clock()

print total
print "Time taken: ", end-start, " s"
