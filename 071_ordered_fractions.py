# Finds the numerator of the largest fraction < 3/7,
# with a denominator <= 1000000

import time

start = time.time()

max_num = 0
max_denom = 1

for denom in range(1000001):
    # If the denominator is divisible by 7, the closest fraction to 3/7 with
    # that denominator will be 3/7 itself, so we skip it
    if denom%7 != 0:
        # Note that this uses integer division, so the fraction will be rounded
        # down
        # This gives us the largest numerator that gives a fraction < 3/7
        num = (3*denom)//7
        # Check if new fraction is larger
        if num*max_denom > denom*max_num:
            max_num = num
            max_denom = denom

end = time.time()

print(max_num)
print("Time taken: ", end-start, "s", sep="")
