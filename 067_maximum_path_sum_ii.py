# Calculates the maximum value path from the top to the bottom of the triangle
# in external_files/067_triangle.txt

from time import clock
import math

start = clock()

f = open("external_files/067_triangle.txt","r")
triangle = [int(x) for x in f.read().split()]
f.close()

# Inverse of the formula for triangular numbers:
# T_n = n*(n+1)/2
num_rows = int(0.5*(math.sqrt(8*len(triangle)+1)-1))

# Cycles through the numbers and increases them by the largest of their two
# upper neighbours. This effectively replaces each number in the triangle by
# the maximum value a path can take that ends at that number. Then all we need
# to do is find the maximum value on the last row.
for i in range(1,num_rows):
    triangle[i*(i+1)/2] += triangle[i*(i-1)/2]
    for j in range(1,i):
        triangle[i*(i+1)/2+j] += max(triangle[i*(i-1)/2+j],triangle[i*(i-1)/2+j-1])
    triangle[i*(i+1)/2+i] = triangle[i*(i-1)/2+i-1] + triangle[i*(i+1)/2+i]

end = clock()

print max(triangle[-num_rows:])
print "Time taken: ", end-start, " s"
