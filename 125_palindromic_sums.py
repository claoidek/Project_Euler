# Finds the sum of all numbers under 10^8 that are both palindromes and can be
# written as the sum of consecutive squares

from time import clock

# Creates palindromes by concatenating numbers with their reverses, as well as
# the reverse of all but their last digit
def create_palindromes(n):
    str_n = str(n)
    palindromes.add(int(str_n + str_n[::-1]))
    palindromes.add(int(str_n + str_n[-2::-1]))

def check_square_sum(n):
    root = 1
    while root*root + (root + 1)*(root + 1) <= n:
        running_total = n - root*root
        next_root = root + 1
        while running_total > 0:
            running_total -= next_root*next_root
            next_root += 1
        if running_total == 0:
            return True
        root += 1
    return False

start = clock()

palindromes = {1,2,3,4,5,6,7,8,9}
total = 0

# Generate all palindromes up to 10^8
for i in range(1,10**5):
    create_palindromes(i)
   
found = set()
root = 1

# Runs through all sums of consecutive squares that are <10^8 and checks if
# they're palindromes
while root*root + (root + 1)*(root + 1) < 10**8:
    running_total = root*root + (root + 1)*(root + 1)
    next_root = root + 2
    while running_total < 10**8:
        if running_total in palindromes:
            found.add(running_total)
        running_total += next_root*next_root
        next_root += 1
    root += 1

end = clock()

print sum(found)
print "Time taken: ", end-start, " s"
