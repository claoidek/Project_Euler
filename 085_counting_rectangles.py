# Finds the area of a grid that contains as close to two million subrectangles
# as possible

import time

def sub_rectangles(m,n):
    total = 0
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            total += (m - i + 1)*(n - j + 1)
            # Return early if we already have too many subrectangles
            if total - num_solutions > min_solution_diff:
                return total
    return total

start = time.clock()

min_solution_diff = 999999
num_solutions = 2000000

for m in range(1,101):
    for n in range(1,m + 1):
        solutions = sub_rectangles(m,n)
        if abs(num_solutions - solutions) < min_solution_diff:
            min_solution_diff = abs(num_solutions - solutions)
            answer = m*n

end = time.clock()

print answer
print "Time taken: ", end-start, " s"
