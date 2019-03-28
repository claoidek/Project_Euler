#

import time
import itertools

def generate_numbers(index):
    n = 1
    num = 1
    while num < 10000:
        num = int(n*coefficients[index][0]*(n*coefficients[index][1] + coefficients[index][2]))
        n += 1
        if num >= 1000 and num < 10000:
            allnums[index].append(str(num))

start = time.clock()

allnums = [[],[],[],[],[],[]]

coefficients = [[0.5,  1,  1], \
                [  1,  1,  0], \
                [0.5,  3, -1], \
                [  1,  2, -1], \
                [0.5,  5, -3], \
                [  1,  3, -2]]

for i in range(6):
    generate_numbers(i)

for perm in itertools.permutations([1,2,3,4,5]):
    for one in allnums[0]:
        for two in allnums[perm[0]]:
            if one[2:] == two[:2]:
                for three in allnums[perm[1]]:
                    if two[2:] == three[:2]:
                        for four in allnums[perm[2]]:
                            if three[2:] == four[:2]:
                                for five in allnums[perm[3]]:
                                    if four[2:] == five[:2]:
                                        for six in allnums[perm[4]]:
                                            if five[2:] == six[:2]:
                                                if six[2:] == one[:2]:
                                                    print int(one)+int(two)+int(three)+int(four)+int(five)+int(six)

end = time.clock()

print "Time taken: ", end-start, " s"
