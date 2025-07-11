# A bouncy number is a number such that the sequence formed by its digits both
# increases and decreases at some point
# This program returns the first number for which the proportion of bouncy
# numbers less than or equal to it is 99%

import time

def is_bouncy(num):
    # If a number starts with a bouncy number, then it too will be bouncy
    if int(str(num)[:-1]) in bouncies:
        return True

    # Iterates over digits and returns when both an increase and decrease have
    # been recorded
    num_list = [int(x) for x in str(num)]
    tracker = 0
    for index, digit in enumerate(num_list[1:]):
        if digit > num_list[index]:
            if tracker == 2:
                return True
            elif tracker == 0:
                tracker = 1
        elif digit < num_list[index]:
            if tracker == 1:
                return True
            elif tracker == 0:
                tracker = 2
    return False

start = time.time()

# We are told that the proportion of bouncy numbers for 21780 is 90% so we can
# start from there
num = 21780
bouncy = 19602

bouncies = set()

while 100*bouncy/num != 99:
    num += 1
    if is_bouncy(num):
        bouncies.add(num)
        bouncy += 1



end = time.time()

print(num)
print("Time taken: ", end-start, "s", sep="")
