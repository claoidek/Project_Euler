# Finds the largest palindromic number that can be made from the product of two
# 3-digit numbers

import time

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

start = time.clock()

num_digits = 3
largest_palindrome = 0

for i in range(10**(num_digits-1),10**num_digits):
    for j in range(10**(num_digits-1),i+1):
        if i*j > largest_palindrome and is_palindrome(i*j):
            largest_palindrome = i*j

end = time.clock()

print largest_palindrome
print "Time taken: ", end-start, " s"
