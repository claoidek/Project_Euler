# Determines a score for each word in the file external_files/042_words.txt by
# summing the position of each of its letters in the alphabet
# The program returns the number of words with a score that is a triangular
# number

import time
import math

# Simple test for square numbers
# This won't work for very large numbers
def is_square(n):
    if int(math.sqrt(n))**2 == n:
        return True
    return False

start = time.time()

f = open("external_files/042_words.txt","r")
words = f.read().split(",")
f.close()

total = 0

for word in words:
    score = sum(ord(i)-64 for i in word[1:-1])
    # x is triangular iff 8*x + 1 is square
    if is_square(8*score + 1):
        total += 1

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
