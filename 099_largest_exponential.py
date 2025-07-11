# Finds the base and exponent combination in external_files/099_base_exp.txt
# that give the largest number
# We use the fact that if a^b > c^d, then b*log(a) > d*log(c), which is much
# easier to calculate

import time
from math import log

start = time.time()

with open("external_files/099_base_exp.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
base_exps = []
for line in lines:
    base_exps.append(line.split(","))

biggest = 0
line_number = -1

for index,[base,exp] in enumerate(base_exps):
    term = float(exp)*log(float(base))
    if term > biggest:
        biggest = term
        line_number = index + 1

end = time.time()

print(line_number)
print("Time taken: ", end-start, "s", sep="")
