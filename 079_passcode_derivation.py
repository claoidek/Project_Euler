# Finds the shortest number that contains the digits of each of the triplets in
# external_files/079_keylog.txt in order (not necessarily consecutively)
# This code only works if there are no repeated digits

import time
import itertools

start = time.clock()

with open('external_files/079_keylog.txt') as f:
    logs = f.read().splitlines()

digits = set()
password = []
digits_before = [[0 for x in range(10)] for x in range(10)]

for log in logs:
    # Tracks digits present in the file
    for digit in log:
        digits.add(int(digit))
    # Tracks the relative ordering of pairs of digits
    for a,b in itertools.combinations(log,2):
        digits_before[int(a)][int(b)] = 1

# The number of other digits each digit must appear before
counts = [sum(x) for x in digits_before]

# Appends digits in the correct order, but only if they are present in the file
for i in range(9,-1,-1):
    for index,count in enumerate(counts):
        if count == i and index in digits:
            password.append(index)

end = time.clock()

print "".join([str(x) for x in password])
print "Time taken: ", end-start, " s"
