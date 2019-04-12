# Finds the number of ways one hundred can be written as a sum of at least two
# positive integers

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
    partitions[n] = total
    return total

start = clock()

partitions = {0:1}

# The function includes the representation with only one integer, so we deduct
# that from the total
total = partition(100)-1

end = clock()

print total
print "Time taken: ", end-start, " s"
