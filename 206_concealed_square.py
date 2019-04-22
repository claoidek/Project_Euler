# Finds the unique number whose square is in the form 1_2_3_4_5_6_7_8_9_0

from time import clock

start = clock()

# For the square to be a 19 digit number, the number itself must have 10 digits
i = 10**9 + 30

while i < 10**10:
    if str(i*i)[0::2] == "1234567890":
        break
    # The number must end in either 30 or 70 for its square to end in 900, so
    # this increment means we only check those numbers
    if i%100 == 30:
        i += 40
    else:
        i += 60

end = clock()

print i
print "Time taken: ", end-start, " s"
