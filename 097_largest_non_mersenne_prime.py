# Prints the last ten digits of the number 28433*2^7830457 + 1

import time

start = time.time()

answer = (28433*2**7830457+1)%10000000000

end = time.time()

print(answer)
print("Time taken: ", end-start, "s", sep="")

