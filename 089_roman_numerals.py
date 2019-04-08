# 

import time

start = time.clock()

with open("external_files/089_roman.txt") as f:
    numerals = f.readlines()
    
numerals = [x.strip() for x in numerals]

characters_saved = 0

for index, numeral in enumerate(numerals):
    if "VIIII" in numerals[index]:
        numerals[index] = numerals[index].replace("VIIII","IX")
        characters_saved += 3
    if "IIII" in numerals[index]:
        numerals[index] = numerals[index].replace("IIII","IV")
        characters_saved += 2
    if "LXXXX" in numerals[index]:
        numerals[index] = numerals[index].replace("LXXXX","XC")
        characters_saved += 3
    if "XXXX" in numerals[index]:
        numerals[index] = numerals[index].replace("XXXX","XL")
        characters_saved += 2
    if "DCCCC" in numerals[index]:
        numerals[index] = numerals[index].replace("DCCCC","CM")
        characters_saved += 3
    if "CCCC" in numerals[index]:
        numerals[index] = numerals[index].replace("CCCC","CD")
        characters_saved += 2

end = time.clock()

print characters_saved
print "Time taken: ", end-start, " s"
