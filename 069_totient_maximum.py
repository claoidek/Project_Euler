# Finds the n <= 1000000 for which n/phi(n) is maximised
# Phi is Euler's Totient function, which is defined here:
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# In order for n/phi(n) to be maximised, we need phi(n) to be minimised
# For this to be true we want as many numbers as possible to share prime factors
# with n
# Using this, we simply multiply the smallest primes until we get a total that
# will be >1000000 if multiplied by the next prime
# This maximised the number of prime factors, and hence, gives us our answer

from time import clock

def is_prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
        return False

    for prime in primes:
        if prime*prime>num:
            return True
        if num%prime == 0:
            return False
    
    i = primes[-1]
    while(i*i <= num):
        if num%i == 0:
            return False
        i += 2
    return True

start = clock()

primes = [2]
total = 2
i = 3

while(i*total <= 1000000):
    if is_prime(i):
        total *= i
        primes.append(i)
    i += 2

end = clock()

print total
print "Time taken: ", end-start, " s"
