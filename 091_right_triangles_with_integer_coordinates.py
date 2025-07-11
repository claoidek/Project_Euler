# Gives the number of right-angled triangles that can be formed under the
# following constraints:
# One point at the origin
# Both other points at integer coordinates
# All coordinates in the range 0-50

import time
import itertools
from fractions import Fraction

start = time.time()

max_coord = 50
# We can work out the number of triangles where the right angle is situated on
# either the horizontal or vertical axes analytically, so we start the
# coordinate range at 1
coord_range = range(1,max_coord + 1)

# We intialise the counter at the number of triangles where the right angle is
# situated on one of the axes
# This will be the case if both other points are on different axes, which gives
# us n^2 combinations (where n is the maximum coordinate)
# There are also n^2 combinations where one point is on the x axis, and forms a
# vertical line with the other
# Finally, there are n^2 combinations where one point is on the y-axis, and
# forms a horizontal line with the other, giving 3n^2 in total
right_angles = 3*max_coord*max_coord

for P in itertools.combinations_with_replacement(coord_range,2):
    slope = Fraction(P[1],P[0])
    # For a right angle to be formed, the slope of PQ must be the negative
    # inverse of the slope of OP
    # We simply move along this line to find integer coordinates and stop once
    # we are outside of the range 0-50
    Q = [P[0] + slope.numerator, P[1] - slope.denominator]
    while max(Q) <= max_coord and min(Q) >= 0:
        # Every triangle has a pair which is formed by flipping the axes, so we
        # increment the count by 2
        right_angles += 2
        Q[0] += slope.numerator
        Q[1] -= slope.denominator

    # We only move in the opposite direction if P is not on the main diagonal
    # If P is on the main diagonal then we will only find triangles that are
    # mirrors of those already found, which we have already accounted for by
    # incrementing the counter by 2
    if P[0] != P[1]:
        Q = [P[0] - slope.numerator, P[1] + slope.denominator]
        while max(Q) <= max_coord and min(Q) >= 0:
            right_angles += 2
            Q[0] -= slope.numerator
            Q[1] += slope.denominator

end = time.time()

print(right_angles)
print("Time taken: ", end-start, "s", sep="")
