# Finds the largest pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2,...,n), where n>1
# This program works by iterating over all pandigital 9-digit number from
# largest to smallest, and testing if they can be written as concatenated
# products

from time import clock
import itertools

start = clock()

found = False

for perm in itertools.permutations([9,8,7,6,5,4,3,2,1]):
    for base_digits in range(1,5):
        # Creates a list version of the permutation so we can delete bits of it
        # later
        list_perm = list(perm)
        n = 2
        # The base for the products
        base = int("".join([str(x) for x in list_perm[:base_digits]]))
        # Remove the base from the list
        del list_perm[:base_digits]

        while len(list_perm) != 0:
            # Find the product of the base with the current n and convert to
            # list
            product = [int (x) for x in str(base*n)]
            # If that product is the next sequence of digits in the list then
            # remove it from the head of the list and increase n for the next
            # product. If not, then this permutation is invalid with this base.
            if product == list_perm[:len(product)]:
                del list_perm[:len(product)]
                n += 1
            else:
                break

        if len(list_perm) == 0:
            found = True
            break

    if found:
        break

end = clock()

print "".join([str(x) for x in perm])
print "Time taken: ", end-start, " s"
