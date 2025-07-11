# Finds the number of characters that would be saved by writing the Roman
# numerals in external_files/089_roman.txt in their minimal form

import time

start = time.time()

with open("external_files/089_roman.txt") as f:
    numerals = f.readlines()
    
numerals = [x.strip() for x in numerals]

characters_saved = 0

# The order of the replacements is significant, as we must check VIIII before
# IIII etc.
replacements = [["VIIII","IX"],["IIII","IV"],["LXXXX","XC"], \
                ["XXXX","XL"],["DCCCC","CM"],["CCCC","CD"]]

for index,numeral in enumerate(numerals):
    for replacement in replacements:
        if replacement[0] in numerals[index]:
            numerals[index] = \
                    numerals[index].replace(replacement[0],replacement[1])
            characters_saved += len(replacement[0]) - len(replacement[1])

end = time.time()

print(characters_saved)
print("Time taken: ", end-start, "s", sep="")
