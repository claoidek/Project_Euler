# Finds the largest prime factor of the number 600851475143

from time import clock

start = clock()

num = 600851475143

i = 3
while num != 1:
    while num%i == 0:
        num = num/i
        largest_factor = i
    i += 2

end = clock()

print largest_factor
print "Time taken: ", end-start, " s"
