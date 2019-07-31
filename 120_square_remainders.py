# Finds the sum of the maximum remainders produced when (a-1)^n+(a+1)^n is
# divided by a^2, in the range 3<=a<=1000
from time import clock

start = clock()

sum_rmax = 0

# It can be seen by expanding (a-1)^n+(a+1)^n that the last term in the
# expansion is 2 for even n and 2an for odd n. All other terms have order >=2
# so they are equal to 0 mod a^2. Hence, we only need to consider the
# contribution of the last term. This means we want to choose n to maximise
# 2an mod a^2. We can see that the expression is minimised when 2an=a^2, or
# n=a/2. Therefore, for a given a, the expression will be maximised when 
# n=(a-1)/2. (We want n to be as big as possible without going over the boundary
# of n=a/2). Therefore, the maximum value of the remainder 2an is 2a((a-1)/2)
for a in range(3,1001):
    sum_rmax += 2*a*((a - 1)/2)

end = clock()

print sum_rmax
print "Time taken: ", end-start, " s"
