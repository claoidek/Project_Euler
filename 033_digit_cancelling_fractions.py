# Finds the denominator of the product of all fractions that satisfy the
# cancelling method described at https://projecteuler.net/problem=33

import time
from fractions import Fraction

# Checks if cancelling two of the digits maintains the value of the fraction
def cancel(a,b):
    if str(a)[0] == str(b)[1]:
        canceled_frac = Fraction(int(str(a)[1]),int(str(b)[0]))
        if Fraction(a,b) == canceled_frac:
            return True
    if str(a)[1] == str(b)[0] and str(b)[1] != "0":
        canceled_frac = Fraction(int(str(a)[0]),int(str(b)[1]))
        if Fraction(a,b) == canceled_frac:
            return True

start = time.time()

valid_fractions = []

for a in range(11,99):
    for b in range(a+1,100):
        if cancel(a,b):
            valid_fractions.append([a,b])

product = 1
for a,b in valid_fractions:
    product *= Fraction(a,b)

end = time.time()

print(product.denominator)
print("Time taken: ", end-start, "s", sep="")
