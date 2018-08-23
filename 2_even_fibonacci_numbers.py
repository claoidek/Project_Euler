# Computes the sum of all even-valued Fibonacci numbers below 4000000
# Uses the closed form for Fibonacci numbers:
# F(n) = (phi^n - (-phi)^-n)/sqrt(5)

import time
import math

start = time.clock()

phi = (math.sqrt(5)+1)/2

term = 1
n = 2
total = 0

while term < 4000000:
    if term%2==0:
        total += term
    term =int((phi**n - (-phi)**-n)/math.sqrt(5))
    n += 1

end = time.clock()

print total
print "Time taken: ", end-start, " s"
