# Finds all N <= 10000 for which the period of the continued fraction for
# sqrt(N) is odd

import math
import time

# Finds the period of the continued fraction representation of sqrt(num)
# Uses the algorithm found here:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def period(num):
    m = 0
    d = 1
    a = math.floor(math.sqrt(num))
    b = a
    period = 0

    while b != 2*a:
        period += 1
        m = d*b - m
        d = (num - m*m)/d
        b = math.floor((a + m)/d)
    return period

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    return False
    
start = time.time()

total = 0

for i in range(2,10001):
    if not is_square(i):
        if period(i)%2 == 1:
            total += 1

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
