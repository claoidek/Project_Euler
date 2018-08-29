import time

start = time.clock()

num = 600851475143

i = 3
while num != 1:
    while num%i == 0:
        num = num/i
        largest_factor = i
    i += 2

print largest_factor

end = time.clock()

print "Time taken: ", end-start, " s"
