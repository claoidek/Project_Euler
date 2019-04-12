# Finds all Lychrel numbers under 10000
# A Lychrel number is a number that never produces a palindrome when iteratively
# adding its reverse to itself
# For example, 349 is not a Lychrel number because:
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337, which is a palindrome

from time import clock

def is_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    return False

start = clock()

total = 9999

for i in range(1,10000):
    iters = 1
    num = i
    # We assume a number is a Lychrel number if it takes more than 50 iterations
    # to reach a palindrome
    while iters < 50:
        iters += 1
        num += int(str(num)[::-1])
        if is_palindrome(num):
            total -= 1
            break

end = clock()

print total
print "Time taken: ", end-start, " s"
