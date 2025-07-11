# Finds the maximum 16-digit string that forms a solution to a magic 5-gon ring
# Explanation at https://projecteuler.net/problem=68

import time
import itertools

def next_index(index):
    return (index + 1)%5

# Checks a ring to see if it's "magic"
def check_ring(ins,outs):
    base = outs[0]+ins[0]+ins[1]
    for i in range(1,5):
        if outs[i]+ins[i]+ins[next_index(i)] != base:
            return False
    return True

start = time.time()

outs = [None]*5
ins = [None]*5
# One of the outer numbers has to be 10 to end up with a 16-digit answer
outs[0] = 10
reps = set()

# Loop over all permutations of the numbers 1-9
for perms in itertools.permutations(range(1,10)):
    # Split the 9 numbers into 4 outer and 5 inner numbers
    outs[1:] = perms[:4]
    ins = perms[4:]

    if check_ring(ins,outs):
        min_out = 11
        min_out_index = 5
        # Find minimum outer number
        for i in range(5):
            if min_out > outs[i]:
                min_out = outs[i]
                min_out_index = i
        # Record unique string for this ring
        term = ""
        for i in range(5):
            index = (min_out_index + i)%5
            triplet = [outs[index],ins[index],ins[next_index(index)]]
            term += "".join(str(x) for x in triplet)
        reps.add(int(term))


# Find maximum string
maximum = 0
for rep in reps:
    if rep > maximum:
        maximum = rep

end = time.time()

print(maximum)
print("Time taken: ", end-start, "s", sep="")
