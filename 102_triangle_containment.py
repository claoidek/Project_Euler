# Finds the number of triangles defined in the file
# external_files/102_triangles.txt that contain the origin

import time
import numpy

# We define a vector pointing along the line |ab| and two more pointing from a
# point on that line to the other two points
# Those two points are on the same side of the line iff the cross products of
# the last two vectors with the first have the same sign
def same_side(p1,p2,a,b):
    cross1 = numpy.cross(b-a,p1-a)
    cross2 = numpy.cross(b-a,p2-a)
    if numpy.dot(cross1,cross2) >= 0.0:
        return True
    return False

# A triangle contains the origin iff for any two vertices, the third vertex and
# the origin are on the same side of the line defined by those vertices
def contains_origin(A,B,C):
    origin = numpy.array([0,0,0])
    if not same_side(origin,C,A,B):
        return False
    if not same_side(origin,B,C,A):
        return False
    if not same_side(origin,A,B,C):
        return False
    return True

start = time.time()

with open("external_files/102_triangles.txt") as f:
    lines = [x.strip() for x in f.readlines()]

points = [line.split(",") for line in lines]

total = 0

for triangle in points:
    A = numpy.array([int(triangle[0]),int(triangle[1]),0])
    B = numpy.array([int(triangle[2]),int(triangle[3]),0])
    C = numpy.array([int(triangle[4]),int(triangle[5]),0])
    if contains_origin(A,B,C):
        total += 1

end = time.time()

print(total)
print("Time taken: ", end-start, "s", sep="")
