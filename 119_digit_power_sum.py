# Finds the 30th entry in the sequence of numbers that are equal to the sum of
# their digits raised to some power

from time import clock

def sum_of_digits(num):
    return sum([int(x) for x in str(num)])

def add_to_list(num):
    if len(valid_nums) < num_to_find:
        valid_nums.add(num)
    elif num < max(valid_nums):
        valid_nums.remove(max(valid_nums))
        valid_nums.add(num)
        upper_limit = max(valid_nums)

start = clock()

upper_limit = 999999999999999

valid_nums = set()
num_to_find = 30

# Loops over bases and exponents and checks if any of the results are have digit
# sums equal to the base
# Only loops up to 100, so theoretically there could be some larger bases that
# produce smaller answers than the ones we've found, but this turns out not to
# be the case
for base in range(2,101):
    for exp in range(2, 101):
        large_num = base**exp
        if large_num >= upper_limit:
            break
        if sum_of_digits(large_num) == base:
            add_to_list(large_num)

end = clock()

print max(valid_nums)
print "Time taken: ", end-start, " s"
