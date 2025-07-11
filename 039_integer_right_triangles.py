# Finds the value of p<=1000 for which the number of right angle triangles with
# perimeter p is maximised

import time

start = time.time()

num_sols = {}
# List of squares for quick lookup
squares = [x*x for x in range(501)]

# For a triangle with perimeter 1000, the two short sides must be < 500
for a in range(2,500):
    # Choose b<a to avoid double counting the same triples
    for b in range(1,a):
        c_sqr = a*a + b*b
        if c_sqr in squares:
            p = a + b + squares.index(c_sqr)
            if p > 1000:
                break
            if p in num_sols:
                num_sols[p] += 1
            else:
                num_sols[p] = 1


end = time.time()

print(max(num_sols, key = num_sols.get))
print("Time taken: ", end-start, "s", sep="")
