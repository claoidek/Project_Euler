# Calculates the sum of the digits of 2^1000

from time import clock

def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

start = clock()

num = 2**1000
answer = sum_of_digits(num)

end = clock()

print answer
print "Time taken: ", end-start, " s"
