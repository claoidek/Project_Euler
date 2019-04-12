# Finds the last ten digits in the sum:
# 1^1 + 2^2 + 3^3 + ... + 1000^1000

from time import clock

start = clock()

total = 0

for i in range(1,1001):
    total += i**i

end = clock()

print str(total)[-10:]
print "Time taken: ", end-start, " s"
