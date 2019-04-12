# finds the smallest value of n for which the number of ways that n objects can
# be separated into piles is divisible by a million

from time import clock


# This is Euler's generating function for partition numbers, which is formula 14
# here:
# http://mathworld.wolfram.com/PartitionFunctionP.html
def partition(n):
    if n in partitions:
        return partitions[n]
    total = 0
    k = 1
    while k*(3*k - 1)/2 <= n:
        total += ((-1)**(k - 1))* \
               (partition(n - (k*(3*k - 1))/2) + partition(n - (k*(3*k + 1))/2))
        k += 1
    
    partitions[n] = total%1000000
    return total%1000000

start = clock()

partitions = {0:1}

i = 1

while partition(i) != 0:
    i += 1

end = clock()

print i
print "Time taken: ", end-start, " s"
