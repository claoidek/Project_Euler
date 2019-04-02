#

import time
import itertools

def next_index(index):
    return (index + 1)%5

def check_ring(ins,outs):
    base = outs[0]+ins[0]+ins[1]
    for i in range(1,5):
        if outs[i]+ins[i]+ins[next_index(i)] != base:
            return False
    return True

start = time.clock()

outs = [None]*5
ins = [None]*5
# One of the outer numbers has to be 10 to end up with a 16-digit answer
outs[0] = 10
reps = []
str_reps = []
term = []

for perms in itertools.permutations(range(1,10)):
    outs[1:] = perms[:4]
    ins = perms[4:]
    if check_ring(ins,outs):
        del term[:]
        min_out = 11
        min_out_index = 5
        for i in range(5):
            if min_out > outs[i]:
                min_out = outs[i]
                min_out_index = i
        for i in range(5):
            index = (min_out_index + i)%5
            term.append([outs[index],ins[index],ins[next_index(index)]])
        reps.append(term)

for rep in reps:
    base = ''
    for triplet in rep:
        for num in triplet:
            base += ''.join(str(num))
    str_reps.append(base)

maximum = 0
for str_rep in str_reps:
    if int(str_rep) > maximum:
        maximum = int(str_rep)
end = time.clock()

print maximum
print "Time taken: ", end-start, " s"
