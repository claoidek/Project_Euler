# Prints the last ten digits of the number 28433*2^7830457 + 1

from time import clock

start = clock()

answer = (28433*2**7830457+1)%10000000000

end = clock()

print answer
print "Time taken: ", end-start, " s"

