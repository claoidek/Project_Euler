# Finds the sum of the digits in the numerator of the 100th convergent of the
# continued fraction for e

from time import clock
from fractions import Fraction

# Contructs the convergent for the given terms of the continued fraction
def big_frac(terms):
    base = Fraction(terms[-1],1)
    for i in range(len(terms)-2,-1,-1):
        base = base**(-1)
        base += terms[i]
    return base

# Returns the first n terms of the continued fraction for e
def e_terms(n):
    out = [2,1,2]
    double = 2
    for j in range(n-3):
        if j%3 < 2:
            out.append(1)
        else:
            out.append(double*2)
            double += 1
    return out
        
start = clock()

total = sum([int(x) for x in str(big_frac(e_terms(100)).numerator)])

end = clock()

print total
print "Time taken: ", end-start, " s"
