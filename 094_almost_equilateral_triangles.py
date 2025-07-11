# An almost equilateral triangle is one where two sides are the same, and the
# other differs in length by 1
# This program finds the sum of the perimeters of all almost equilateral
# triangles whose side lengths and area are all integers, and whose perimeter
# does not exceed one billion

# We solve this by dividing the isosceles triangle into two right triangles
# We need to generate pythagorean triples a,b,c, with a<b<c, such that
# abs(2*a-c) = 1
# We can't have abs(2*b-c) = 1 because the longest leg of a right triangle is
# always >=1/sqrt(2) = ~0.7 of the hypotenuse
# It is enough to generate primitive pythagorean triples, as if we use a
# non-primitive triple a*k,b*k,c*k, we would need abs(2*a*k - c*k) = 1
# This implies abs(2*a-c) = 1/k, which is impossible for k>1 since a and c are
# integers
import time
from math import sqrt

start = time.time()

max_perim = 1000000000
total = 0
m = 2

# We use Euclid's formula to generate the triples:
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# However, since we have a restriction on one of the sides, we do not need to
# try every n
# The shortest leg will be equal to either m^2 - n^2 or 2*m*n
# This means that we need either abs(m*m + n*n - 2(m*m - n*n)) = 1 or 
# abs(m*m + n*n - 2(2*m*n)), which simplify to abs(m^2 - 3 n^2) = 1 and
# abs(m^2 - 4 m n + n^2) = 1 respectively
# Solving these for n we get n = sqrt(m^2 +/- 1)/sqrt(3) and 
# n = 2 m - sqrt(3 m^2 +/- 1) respectively
# We therefore only have to check 4 values of n for each m
while 4*m*m <= max_perim:
    # Ideally we would just check if any of the four possibilities were
    # integers, but rounding and floating point errors make this difficult
    # Instead we just get the integer part of all of them, and check if they
    # give a valid combination
    possible_ns = set([int(sqrt(m*m - 1)/sqrt(3)), \
                       int(sqrt(m*m + 1)/sqrt(3)), \
                       int(2*m - sqrt(3*m*m - 1)), \
                       int(2*m - sqrt(3*m*m + 1))])
    for n in possible_ns:
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        base = min(a,b)
        if abs(2*base - c) == 1:
            total += 2*c + 2*base
    m += 1

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
