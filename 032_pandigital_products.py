# Finds the sum of all numbers c that can be written in the form a*b = c such
# that the concatened number abc contains each of the digits from 1 to 9 
# exactly once (and no 0's).

import time

def is_pandigital(string):
    # A number fits our criteria if its length remains unchanged after removing
    # duplicates, and does not contain any 0's
    if len(string) == len(set(string)) and "0" not in string:
        return True
    return False

def find_products(len_a,len_b,len_prod):
    for a in range(10**(len_a-1),10**(len_a)):
        for b in range(10**(len_b-1),10**(len_b)):
            if len(str(a*b)) > len_prod:
                break
            if is_pandigital(str(a)+str(b)+str(a*b)):
                products.add(a*b)

start = time.time()

products = set()

# These are the only combinations of lengths of factors and product such that
# the total length is 9
find_products(2,3,4)
find_products(1,4,4)

end = time.time()

print(sum(products))
print("Time taken: ", end-start, "s", sep="")
