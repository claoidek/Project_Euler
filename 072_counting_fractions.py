# Finds the number of reduced proper fractions with denominator <= 1000000
# This is the same as finding the length of the Farey sequence of order 1000000
# https://en.wikipedia.org/wiki/Farey_sequence

from time import clock

# We use a recursive formula to find the length of the Farey sequence
# The details of this formula are here:
# https://en.wikipedia.org/wiki/Farey_sequence#Sequence_length_and_index_of_a_fraction
def farey(n):
    if n in fdict:
        return fdict[n]
    # This relies on integer division
    base = n*(n+3)/2
    for d in range(2,n+1):
        # So does this
        term = n/d
        new_farey = farey(term)
        fdict[term] = new_farey
        base -= new_farey
    return base

start = clock()

fdict = {1:2}
# The Farey sequence includes 0 and 1, so we subtract 2 to account for them
answer = farey(1000000)-2

end = clock()

print answer
print "Time taken: ", end-start, " s"
