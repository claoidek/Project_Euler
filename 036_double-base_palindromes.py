# Finds the sum of all numbers less than a million that are palindromes in both
# base 10 and base 2

from time import clock

def is_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    return False

# Converts base 10 numbers to base 2
def b10_to_b2(num):
    b2_rep = [1]
    power = 0
    
    while 2**power <= num:
        power += 1
    power -= 1
    num -= 2**power

    while power != 0:
        power -= 1
        if num >= 2**power:
            b2_rep.append(1)
            num -= 2**power
        else:
            b2_rep.append(0)

    return int("".join([str(x) for x in b2_rep]))

start = clock()

total = 0

# We only need to check odd numbers, as even numbers end in 0 in binary (and all
# numbers must start with 1)
for i in range(1,1000001,2):
    if is_palindrome(i):
        if is_palindrome(b10_to_b2(i)):
            total += i

end = clock()

print total
print "Time taken: ", end-start, " s"
