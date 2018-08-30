# Finds the product a*b*c where a^2 + b^2 = c^2 and a + b + c = 1000
# Uses Euclid's Formula (https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)

import time

start = time.clock()

found = False
m = 2

while not found:
    for n in range(1,m):
        base_a = m*m - n*n
        base_b = 2*m*n
        base_c = m*m + n*n
        a = base_a
        b = base_b
        c = base_c
        k = 1
        while a+b+c < 1000:
            k += 1
            a = base_a*k
            b = base_b*k
            c = base_c*k
        if a+b+c == 1000:
            found = True
            break
    m += 1

end = time.clock()

print a*b*c
print "Time taken: ", end-start, " s"
