# Gives the sum of all numbers that cannot be represented as the sum of two
# abundant numbers.
# An abundant number is a number that is less than the sum of its divisors.
# All numbers over 28123 can be represented as the sum of two abundant numbers
# so we do not check numbers over this limit.

from time import clock

def sum_of_proper_divisors(n):
    total = 1
    i = 2
    while i*i < n:
        if n%i == 0:
            total += i + n/i
        i += 1
    
    # Adds last divisor if n is a perfect square
    if i*i == n:
        total += i

    return total

start = clock()

lowest_abundant_number = 12
upper_limit = 28123

total = 0

abundant_numbers =  [i for i in range(lowest_abundant_number, upper_limit-lowest_abundant_number) if i<sum_of_proper_divisors(i)]
abundant_sums = set()

for index, i in enumerate(abundant_numbers):
    for j in abundant_numbers[index:]:
        if i+j <= upper_limit:
            abundant_sums.add(i+j)
        else:
            break

for i in range(1,upper_limit+1):
    if i not in abundant_sums:
        total += i

end = clock()

print total
print "Time taken: ", end-start, " s"
