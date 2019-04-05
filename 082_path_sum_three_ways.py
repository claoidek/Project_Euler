# Finds the minimal path sum in external_files/082_matrix.txt where only
# movements down, up and to the right are permitted
# The starting position can be anywhere in the leftmost column and the ending
# position can be anywhere in the rightmost column

import time
import csv

def get_data():
    rows = []
    with open('external_files/082_matrix.txt') as f:
        reader = csv.reader(f)
        for line in reader:
            rows.append([int(x) for x in line])
    return rows

start = time.clock()

rows = get_data()

# We move through the matrix column by column, from right to left, and top to
# bottom within each column
# For each entry, we find its minimal path sum to the next column and add it to
# the entry
for x in range(len(rows)-2,-1,-1):
    for y in range(len(rows)):
        # Default minimal path is simply moving right into the next column
        min_path = rows[y][x+1]

        # Check if we can improve the minimum by moving up any number of times
        # before moving right
        # Since the minimal path for the entry above has already been computed,
        # we need only check if adding the current entry onto that path is
        # smaller than moving directly to the right
        if y != 0 and rows[y-1][x] < min_path:
            min_path = rows[y-1][x]
        
        # Check if we can improve the minimum by moving down any number of times
        # before moving right
        # The entries further down have not had their paths computed yet so we
        # need to check them all manually
        down_sum = 0
        for d in range(y+1,len(rows)):
            if down_sum + rows[d][x] + rows[d][x+1] < min_path:
                min_path = down_sum + rows[d][x] + rows[d][x+1]
            down_sum += rows[d][x]
        rows[y][x] += min_path

# The answer is the smallest entry in the first column
min_path = rows[0][0]
for row in rows:
    if row[0] < min_path:
        min_path = row[0]

end = time.clock()

print min_path
print "Time taken: ", end-start, " s"
