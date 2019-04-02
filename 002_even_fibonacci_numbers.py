# Computes the sum of all even-valued Fibonacci numbers below 4000000
# Uses the closed form for Fibonacci numbers:
# F(n) = (phi^n - (-phi)^-n)/sqrt(5)

import time
import math

start = time.clock()

phi = (math.sqrt(5)+1)/2

term = 0
n = 0
total = 0

while term < 4000000:
    total += term
    term = int((phi**n - (-phi)**-n)/math.sqrt(5))
    # Uses the fact that every third Fibonacci number is even
    n += 3

end = time.clock()

print total
print "Time taken: ", end-start, " s"
