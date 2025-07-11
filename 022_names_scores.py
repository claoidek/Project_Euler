# Adds up the score of all names in the file external_files/022_names.txt
# First the list is sorted alphabetically
# Then an alphabetical value is determined for each name by summing the position
# of each of its letters in the alphabet
# This value is then multiplied by the name's its position in the alphabetical 
# list to determine the score of that name

import time

start = time.time()

f = open("external_files/022_names.txt","r")
names = f.read().split(",")
f.close()

names.sort()

total = 0

for position, name in enumerate(names):
    total += (position+1)*sum(ord(i)-64 for i in name[1:-1])

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
