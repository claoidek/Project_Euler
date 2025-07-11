# Calculates the sum of the digits of 2^1000

import time

def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

start = time.time()

num = 2**1000
answer = sum_of_digits(num)

end = time.time()

print(answer)
print("Time taken: ", end-start, "s", sep="")
