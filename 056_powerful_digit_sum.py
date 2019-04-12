# Finds the values of a,b<100 that maximise the sum of the digits of a^b

from time import clock

def sum_digits(num):
    return sum([int(x) for x in str(num)])

start = clock()

max_sum = 0

for a in range(1,100):
    for b in range(1,100):
        sum_ab = sum_digits(a**b)
        if sum_ab > max_sum:
            max_sum = sum_ab

end = clock()

print max_sum
print "Time taken: ", end-start, " s"
