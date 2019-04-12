# Finds all primes such that recursively removing digits from either end results
# in only other primes

from time import clock

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
            return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

start = clock()

num_primes = 0
total = 0

# If any of these digits are in the number, they will be at the end of one of
# the truncated numbers, making it non-prime
invalid_digits = ["4","6","8","0"]

# 1 can't begin or end the number as 1 is non-prime
only_in_middle = "1"

# 2 or 5 can be the first digit as they are prime, nut cannot be in any other
# position as all other numbers ending in 2 or 5 are non-prime
only_at_start = ["2","5"]

# Starting value ensures we only check numbers with 2 digits or more
number = 9

# The problem states that there are only 11 such primes
while num_primes < 11:
    valid = True
    number += 2
    string = str(number)
    if any(x in string for x in invalid_digits) or any(x in string[1:] for x in only_at_start):
        continue
    if string[0] == only_in_middle or string[-1] == only_in_middle:
        continue
    if not is_prime(number):
        continue
    for i in range(1,len(string)):
        if not is_prime(int("".join(string[:-i]))) or not is_prime(int("".join(string[i:]))):
            valid = False
            break
    if valid:
        num_primes += 1
        total += number

end = clock()

print total
print "Time taken: ", end-start, " s"
