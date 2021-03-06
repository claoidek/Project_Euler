# Finds the first triangular number with over 500 divisors
# A little slow. The divisors function could be improved.

from time import clock

def divisors(num):
    num_divisors = 0
    i = 1
    while i*i < num:
        if num%i == 0:
            num_divisors += 2
        i += 1

    if i*i == num:
        num_divisors += 1

    return num_divisors

start = clock()

threshold = 500
num_divisors = 0
n = 1

while num_divisors <= threshold:
    triangle = n*(n+1)/2
    num_divisors = divisors(triangle)
    n += 1
end = clock()

print triangle
print "Time taken: ", end-start, " s"
