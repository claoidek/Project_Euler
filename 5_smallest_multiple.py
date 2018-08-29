# Finds the smallest number that is evenly divisible by all numbers from 1 to 20

import time

def prime_factors(num):
    factors = {}
    i = 2
    while num != 1:
        while num%i == 0:
            num = num/i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
        i += 1
    return factors

start = time.clock()

num = 1
upper_bound = 20

all_factors = {}

for i in range(2,upper_bound+1):
    # Find all prime factors of the current divisor
    i_factors = prime_factors(i)

    # Add any new factors to the global set
    # Note that we not only need to track which prime factors are present, we
    # must also track the maximum number of each prime factor needed for the
    # individual divisors
    # e.g. 8 needs three factors of 2, while 2 only needs 1
    for prime in i_factors:
        if prime in all_factors:
            if i_factors[prime] > all_factors[prime]:
                all_factors[prime] = i_factors[prime]
        else:
            all_factors[prime] = i_factors[prime]

# Multiply all factors together to get the minimum number satisfying the constraints
for factor in all_factors:
    num *= factor**all_factors[factor]

end = time.clock()

print num
print "Time taken: ", end-start, " s"
