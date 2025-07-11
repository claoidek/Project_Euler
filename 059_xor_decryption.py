# Finds the three character encryption key and uses it to decrypt the file in
# external_files/059_cipher.txt
# Returns the sum of the ASCII values in the decrypted text

import csv
import time
import itertools

start = time.time()

with open('external_files/059_cipher.txt', 'r') as f:
    encrypted = list(csv.reader(f))[0]

total = 0
# Key is three lower-case characters
limits = range(ord("a"),ord("z")+1)

for product in itertools.product(limits,limits,limits):
    decrypted = ""
    for index, letter in enumerate(encrypted):
        new_code = int(letter)^product[index%3]
        # Checks that only valid characters are generated
        if new_code not in range(32,127):
            decrypted = ""
            break
        decrypted += chr(new_code)
    
    # Checks for common English words
    if all(x in decrypted for x in [" the "," and "," be "," to "]):
        for letter in decrypted:
            total += ord(letter)
        break

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
