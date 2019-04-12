# Finds the number of values <= 1500000 such that there is exactly one way of
# forming a right angle triangle with that perimeter
# Uses Euclid's Formula:
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

from time import clock

start = clock()

# Set of all triples with perimeter <= 1500000
triples = set()

# count of how many triples there are for each perimeter
perims = {}

m = 2
limit = 1500000

# The maximum value for the hypotenuse is m*m - 1, which cannot be greater than
# half the perimeter
while m*m < limit/2:
    for n in range(1,m):
        k = 1
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        if a + b + c > limit:
            break
        # Euclid's Formula doesn't generate all non-primitive triples, so we
        # must add those as well
        while k*(a + b + c) <= limit:
            triples.add(tuple(sorted([k*a,k*b,k*c])))
            k += 1
    m += 1

for triple in triples:
    L = sum(triple)
    if L in perims:
        perims[L] += 1
    else:
        perims[L] = 1
    
total = 0
for L in perims:
    if perims[L] == 1:
        total += 1

end = clock()

print total
print "Time taken: ", end-start, " s"
