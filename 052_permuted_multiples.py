# Finds the smallest number x such that x,2x,3x,...,6x all contain the same
# digits in different orders.

import time

start = time.time()

found = False

num = 1

while not found:
    found = True
    for i in range(2,7):
        if sorted(str(num)) != sorted(str(num*i)):
            found = False
            break
    num += 1

end = time.time()

print(num - 1)
print("Time taken: ", end-start, "s", sep="")
