# Finds the first cube for which four other permutations of its digits are also
# cubes

import time

start = time.clock()

# Dictionary indexed by a sorted tuple of the cube's digits
# The value is a list of two numbers
# The first is the smallest cube with this set of digits
# The second is the number of cubic permutations that have been found
cube_perms = {(1):[1,1]}
n = 1
cube = n**3
key = (1)

while cube_perms[key][1] != 5:
    n += 1
    cube = n**3
    key = tuple(sorted([int(x) for x in str(cube)]))
    if key in cube_perms:
        cube_perms[key][1] += 1
    else:
        cube_perms[key] = [cube,1]

end = time.clock()

print cube_perms[key][0]
print "Time taken: ", end-start, " s"
