# Finds the coefficients a<|1000| and b<=|1000| such that the expression
# n^2 + a*n + b gives the longest possible string of primes, starting from n=0
# The program returns the product a*b.

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

max_n = 0
max_a = 9999
max_b = 9999

for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while is_prime(n*n + a*n + b):
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

end = clock()

print max_a*max_b
print "Time taken: ", end-start, " s"
