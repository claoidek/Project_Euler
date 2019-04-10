# Prints the last ten digits of the number 28433*2^7830457 + 1

import time

start = time.clock()

answer = (28433*2**7830457+1)%10000000000

end = time.clock()

print answer
print "Time taken: ", end-start, " s"

