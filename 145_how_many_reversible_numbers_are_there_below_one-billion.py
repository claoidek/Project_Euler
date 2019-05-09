# Finds the number of integers below one billion that can be added to their
# reverse to produce a number with only odd digits

from time import clock

start = clock()

reversibles = 0

# We solve analytically based on the number of digits n

# Firstly we note that there are 30 choices of pairs of digits that add to an
# odd number less than 10:
#   0 1 2 3 4 5 6 7 8 9
# 0   X   X   X   X   X
# 1 X   X   X   X   X
# 2   X   X   X   X
# 3 X   X   X   X
# 4   X   X   X
# 5 X   X   X
# 6   X   X
# 7 X   X
# 8   X
# 9 X

# 10 of these contain 0 so there are 20 choices that do not
# This is relevant because neither of the outside digits can be 0

# We can also note that there are 20 pairs with an odd sum greater than 10
#   0 1 2 3 4 5 6 7 8 9
# 0
# 1
# 2                   X
# 3                 X
# 4               X   X
# 5             X   X
# 6           X   X   X
# 7         X   X   X
# 8       X   X   X   X
# 9     X   X   X   X

# And finally, 25 pairs with an even sum less than 10
#   0 1 2 3 4 5 6 7 8 9
# 0 X   X   X   X   X
# 1   X   X   X   X
# 2 X   X   X   X
# 3   X   X   X
# 4 X   X   X
# 5   X   X
# 6 X   X
# 7   X
# 8 X
# 9

# If n is even then none of the digit sums can be greater than 9
# We can see this because each pair of digits must be added together twice, and
# must have the same parity each time they are added in order to both be odd
# However, a pair summing to 10 or more will change the parity of the pair
# outside it
# Since this is not allowed, we have 20 choices of pairs for the outside digits
# and 30 choices for each of the other n/2 - 1 pairs, giving 20*30^(n/2 - 1) in
# total

# If n is odd it will be in the form 4*k + 1 or 4*k + 3

# If n is in the form 4*k + 1 then it cannot satisfy the criteria
# We can see this by dividing the number into its middle digit and an
# even-digited number consisting of the remaining digits
# This even-digited number must not have any digit sums greater than 9 for the
# same reasons outlined above
# However this means that the middle digit added to itself would have to be odd,
# which is not possible

# Finally, if n is in the form 4*k + 3 then the middle digit added to itself
# must be less than 10 in order not to change the parity of the pair outside it
# The pair outside it must be an odd pair greater than 10 in order to change the
# parity of the middle pair
# Moving outwards we need to alternate between odd pairs greater than 10 and
# even pairs less than 10 in order to preserve parity all the way through
# This leaves us with 5 choices for the middle digit, 20 choices for the outer
# pair, 20 choices for k of the remaining pairs, and 25 choices for the final k
# pairs
# This gives 100*500^k in total

for num_digits in range(1,10):
    if num_digits%2 == 0:
        reversibles += 20*30**(num_digits/2 - 1)
    elif num_digits%4 == 3:
        k = (num_digits - 3)/4
        reversibles += 100*500**k

end = clock()

print reversibles
print "Time taken: ", end-start, " s"
