# Finds the number of positive integers below 10^100 that have either
# monotonically increasing or decreasing digits (non-bouncy numbers)

import time
import copy

start = time.time()

max_num_digits = 100
# Single digit numbers are all non-bouncy
num_non_bouncy = 9

# Tracks the number of increasing/decreasing numbers starting with each digit
# for the current and previous number of digits
current_decreasing = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
current_increasing = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
prev_decreasing = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
prev_increasing = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}

for digits in range(2,max_num_digits + 1):
    # Numbers which consist of one repeated digit will be double counted as they
    # are both increasing and decreasing, so this line accounts for them
    num_non_bouncy -= 9

    # For every increasing/decreasing number with the previous number of digits,
    # work out how many new increasing/decreasing numbers starting with each
    # digit can be made that end with that number
    # For example, if we have the number 85, we can make the numbers 885 and 985
    for start_digit in range(0,10):
        for new_start in range(start_digit,10):
            current_decreasing[new_start] += prev_decreasing[start_digit]
            # We need to track numbers like 000 so that we can make numbers like
            # 1000 later, but we don't want to add them to the total as they're
            # not real numbers
            if new_start != 0:
                num_non_bouncy += prev_decreasing[start_digit]
    for start_digit in range(0,10):
        for new_start in range(0,start_digit + 1):
            current_increasing[new_start] += prev_increasing[start_digit]
            if new_start != 0:
                num_non_bouncy += prev_increasing[start_digit]
    
    prev_decreasing = copy.deepcopy(current_decreasing)
    prev_increasing = copy.deepcopy(current_increasing)
    for start_digit in range(0,10):
        current_decreasing[start_digit] = 0
        current_increasing[start_digit] = 0

end = time.time()

print(num_non_bouncy)
print("Time taken: ", end-start, "s", sep="")
