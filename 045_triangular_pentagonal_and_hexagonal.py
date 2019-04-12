# Finds the next number after 40755 that is triangular, pentagonal, and
# hexagonal
# All hexagonal numbers are triangular so we don't need to test for that

from time import clock
import math

# Simple test for square numbers
# This won't work for very large numbers
def is_square(n):
    if int(math.sqrt(n))**2 == n:
        return True
    return False

start = clock()

num = 40755
n = 143
found = False

while not found:
    # Generates the next hexagonal number
    num += 4*n + 1
    n += 1
    # Checks if it's also pentagonal
    if is_square(24*num + 1) and math.sqrt(24*num + 1)%6 == 5:
        found = True

end = clock()

print num
print "Time taken: ", end-start, " s"
