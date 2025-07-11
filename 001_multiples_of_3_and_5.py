# Finds the sum of multiples of 3 and 5 below 1000

import time

start = time.time()

total = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        total += i

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
