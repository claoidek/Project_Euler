# Finds the minimal path sum in external_files/081_matrix.txt where only
# movements down and to the right are permitted
# The starting position is in the top-right corner

import time
import csv

def get_data():
    rows = []
    with open('external_files/081_matrix.txt') as f:
        reader = csv.reader(f)
        for line in reader:
            rows.append([int(x) for x in line])
    return rows

start = time.clock()

rows = get_data()

# We move through the matrix in left-to-right, bottom-to-top diagonal strips,
# starting with the bottom-left corner
# For each entry, we add the smaller of its right and down neighbours
# This represents the minimal path from that entry to the bottom-right corner
# After doing this for all entries, the top-left entry will be our answer

# First half of the diagonals
for i in range(len(rows)-2,-1,-1):
    x = i
    y = len(rows)-1
    while x < len(rows):
        if y == len(rows)-1:
            rows[y][x] += rows[y][x+1]
        elif x == len(rows)-1:
            rows[y][x] += rows[y+1][x]
        else:
            rows[y][x] += min(rows[y+1][x],rows[y][x+1])
        x += 1
        y -= 1

# Second half of the diagonals
for i in range(len(rows)-2,-1,-1):
    x = 0
    y = i
    while y > -1:
        rows[y][x] += min(rows[y+1][x],rows[y][x+1])
        x += 1
        y -= 1

end = time.clock()

print rows[0][0]
print "Time taken: ", end-start, " s"
