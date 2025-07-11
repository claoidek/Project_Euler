# Finds the smallest member of the longest chain of amicable numbers with no
# member exceeding one million

import time

start = time.time()

upper_limit = 10**6
sum_of_divisors = [1 for i in range(upper_limit + 1)]

# Sieve generating the sum of proper divisors for all numbers up to the limit
for i in range(2,upper_limit//2 + 1):
    for j in range(2*i,upper_limit,i):
        sum_of_divisors[j] += i

longest_length = 0

for i in range(1,upper_limit+1):
    invalid = False
    chain = []
    num = i

    # Loop until a chain is formed or an invalid number is found
    while num not in chain:
        chain.append(num)
        num = sum_of_divisors[num]
        if num > upper_limit:
            invalid = True
            break

    # Set all members of the chain to an invalid number (i.e. one over the
    # limit) to ensure that they're not calculated again unnecessarily    
    for link in chain:
        sum_of_divisors[link] = upper_limit + 1

    if not invalid:
        length = len(chain) - chain.index(num)
        chain = chain[-length:]

    if length > longest_length:
        longest_length = length
        longest_chain = list(chain)

end = time.time()

print(min(longest_chain))
print("Time taken: ", end-start, "s", sep="")

