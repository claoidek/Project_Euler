# Finds how many of the first 1000 expansions of the square root of two as a
# continued fraction have a numerator with more digits than the denominator.
# The expansion is as follows:
# 1 + 1/2
# 1 + 1/(2 + 1/2)
# 1 + 1/(2 + 1/(2 + 1/2))
# ...
# 1 + 1/(2 + 1/(2 + 1/(2 + ... )))

import time
from fractions import Fraction

start = time.time()

frac = Fraction(1+0.5)
total = 0

for i in range(2,1001):
    frac = 1 + Fraction(1,1+frac)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        total += 1

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
