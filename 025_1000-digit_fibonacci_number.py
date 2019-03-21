# Finds the first Fibonacci number with more than 1000 digits

import time

start = time.clock()

first = 1
second = 1
third = first + second
index = 3
cutoff = 10**999

while third < cutoff:
    index += 1
    first = second
    second = third
    third = first + second

end = time.clock()

print index
print "Time taken: ", end-start, " s"
