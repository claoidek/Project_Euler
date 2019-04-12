# Finds the number under one million that generates the longest Collatz
# sequence (en.wikipedia.org/wiki/Collatz_conjecture)
# Another slow one. Possibly improve using memoisation?

from time import clock

def update(num):
    if num%2 == 0:
        return num/2
    return 3*num + 1

def collatz_sequence_length(num):
    length = 1
    while num != 1:
        num = update(num)
        length += 1
    return length

start = clock()

max_length = 0
max_n = 0
upper_bound = 1000000

for n in range(1,upper_bound+1):
    length = collatz_sequence_length(n)
    if length > max_length:
        max_length = length
        max_n = n

end = clock()

print max_n
print "Time taken: ", end-start, " s"
