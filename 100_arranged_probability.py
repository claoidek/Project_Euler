# Consider a box containing b blue disks and r red disks, and n = b + r
# It is possible to choose b and r such that the probability of two randomly
# chosen different disks both being blue is exactly 1/2
# This program finds the smallest n > 10**12 for which this is possible and
# returns the corresponding value for b

# For the probability to equal 1/2 we need:
# ((b)*(b - 1))/((b + r)*(b + r - 1)) = 1/2
# Solving this for b gives b = (1 + 2r + sqrt(1 + 8r^2))/2
# This means that 1 + 8r^2 must be a perfect square
# The sequence of numbers for which this is true is found here:
# https://oeis.org/A001109
# It can be generated recursively by a(n) = 6*a(n - 1) - a(n - 2)
# a(0) = 0
# a(1) = 1
# This allows us to generate r and b until we get r + b > 10**12

from time import clock
from math import sqrt

def update_red(a_minus_2,a_minus_1):
    return 6*a_minus_1 - a_minus_2

def update_blue(red_disks):
    return int((sqrt(8*red_disks**2 + 1) + 2*red_disks + 1)/2)

start = clock()

a_minus_2 = 0
a_minus_1 = 1
red_disks = update_red(a_minus_2,a_minus_1)
blue_disks = update_blue(red_disks)

while red_disks + blue_disks <= 10**12:
    a_minus_2 = a_minus_1
    a_minus_1 = red_disks
    red_disks = update_red(a_minus_2,a_minus_1)
    blue_disks = update_blue(red_disks)

end = clock()

print blue_disks
print "Time taken: ", end-start, " s"
