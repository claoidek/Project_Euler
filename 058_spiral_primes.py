# Finds the smallest width of a number spiral such that the percentage of
# numbers along both diagonals that are prime is below 10%.
#
# Example of a 5x5 spiral:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# This one is slow due to all the prime-checking. Will be significantly improved
# if there's a faster way to check.

import time

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
            return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

start = time.clock()

spiral_width = 3
last_num = 9
diag_nums = 5
primes = 3

while(float(primes)/diag_nums) > 0.1:
    diag_nums += 4
    spiral_width += 2

    for num in [last_num + x*(spiral_width - 1) for x in range(1,5)]:
        if is_prime(num):
            primes += 1
    
    last_num += 4*spiral_width - 4

end = time.clock()

print spiral_width
print "Time taken: ", end-start, " s"
