# Finds the product of certain digits of Champernowne's constant, as described
# at https://projecteuler.net/problem=40

from time import clock

start = clock()

d = [0]
n = 1

while len(d) < 1000001:
    d += [int(x)for x in str(n)]
    n += 1

total = 1
for power in range(7):
    total *= d[10**power]

end = clock()

print total
print "Time taken: ", end-start, " s"
