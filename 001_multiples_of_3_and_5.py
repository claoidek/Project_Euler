# Finds the sum of multiples of 3 and 5 below 1000

from time import clock

start = clock()

total = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        total += i

end = clock()

print total
print "Time taken: ", end-start, " s"
