# Finds the number of distinct terms that can be represented in the form a^b
# where 2 <= a,b <= 100

from time import clock

start = clock()

distinct_terms = set()

for a in range(2,101):
    for b in range(2,101):
        distinct_terms.add(a**b)

end = clock()

print len(distinct_terms)
print "Time taken: ", end-start, " s"
