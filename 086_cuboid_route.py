# Finds the smallest M such that there exist at least one million cuboids, with
# no side greater than M, where the shortest path along the faces of the cube
# between opposite corners has an integer length 

import time
import math

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    return False

# Returns the number of combinations of two integers y,z <= x that sum to yplusz
def combinations(x,yplusz):
    return min(x + 1,yplusz) - math.ceil(yplusz/2.0)

start = time.time()

x = 0
solutions = 0
threshold = 1000000

# x,y,z are the dimensions of the cuboid
# If x is the longest side, the length of the path is sqrt(x^2 + (y+z)^2)
# This means we can combine y and z into one variable
# However, we also need to account for all the combinations of y and z that have
# the same total, with y,z <= x
# We keep looping, increasing x until we reach one million solutions
while solutions < threshold:
    x += 1
    for yplusz in range(2,x*2 + 1):
        # Check if path length is an integer
        if is_square(x**2 + yplusz**2):
            solutions += combinations(x,yplusz)

end = time.time()
    
print(x)
print("Time taken: ", end-start, "s", sep="")
