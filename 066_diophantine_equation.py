# Finds the D <= 1000 which maximises the minimum x for which a solution to the
# equation x^2 - D*y^2 = 1 exists

 # This is a little slow, due to the time taken to reconstruct the convergent at
 # every iteration (the big_frac function)
 # It would be improved by finding a method to convert the nth convergent into
 # the (n+1)th convergent without recalculating all the terms

import time
import math
from fractions import Fraction

# Contructs the convergent for the given terms of the continued fraction
def big_frac(terms):
    base = Fraction(terms[-1],1)
    for i in range(len(terms)-2,-1,-1):
        base = base**(-1)
        base += terms[i]
    return base

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    return False

# Returns the smallest x for which we can satisfy x^2 - D*y^2 = 1
# This is done by finding the convergents of the continued fraction for
# sqrt(D), and testing them until we find a convergent x/y that satisfies the
# equation
# This method is outlined here:
# http://mathworld.wolfram.com/PellEquation.html
def find_smallest_solution(D):
    m = 0
    d = 1
    a = int(math.floor(math.sqrt(D)))
    b = a
    terms = [a]
    x_y = Fraction(0,1)

    while x_y.numerator**2 - D*(x_y.denominator**2) != 1:
        m = d*b - m
        d = (D - m*m)/d
        b = int(math.floor((a + m)/d))
        terms.append(b)
        x_y = big_frac(terms)
    return x_y.numerator

start = time.time()

maximum = 0
max_D = 0

for D in range(1001):
    if not is_square(D):
        x = find_smallest_solution(D)
        if x > maximum:
            maximum = x
            max_D = D

end = time.time()

print(max_D)
print("Time taken: ", end-start, "s", sep="")
