# 

import time

def factorial_sum(num):
    total = 0
    for digit in str(num):
        total += factorials[int(digit)]
    return total

def chain_length(num):
    length = 1
    prev = {num}
    num = factorial_sum(num)
    if num in master:
        return master[num]
    first_num = num
    while num not in prev:
        prev.add(num)
        num = factorial_sum(num)
    master[first_num] = len(prev)
    return len(prev)

start = time.clock()

master = {}
factorials = [1,1,2,6,24,120,720,5040,40320,362880]

sixties = 0
for i in range(1000001):
    if chain_length(i) == 60:
        sixties += 1

end = time.clock()

print sixties
print "Time taken: ", end-start, " s"
