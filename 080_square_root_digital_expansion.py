# Finds the sum of the first hundred decimal digits in all of the irrational
# square roots of the first hundred natural numbers

import time
import decimal

start = time.clock()

squares = [x*x for x in range(11)]

# Set precision for our square roots
decimal.getcontext().prec = 102

total = 0
for i in range(101):
    if i not in squares:
        root = decimal.Decimal(i).sqrt()
        # Add all of the first 101 characters apart from the decimal point
        total += sum([int(x) for x in str(root)[:101] if x != "."])

end = time.clock()

print total
print "Time taken: ", end-start, " s"
