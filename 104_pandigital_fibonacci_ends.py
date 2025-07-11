# Finds the index of the first Fibonacci number whose first 9 digits and last 9
# digits are both 1-9 pandigital

import time

def is_pandigital(num):
    if len(num) == len(set(num)) and "0" not in num:
        return True
    return False

start = time.time()

first = 0
second = 1
end_digits = first + second
index = 2
phi = (1 + 5**0.5)/2

while end_digits < 10**8:
    index += 1
    first = second
    second = end_digits
    end_digits = first + second

start_digits = end_digits

while True:
    if is_pandigital(str(end_digits)):
        if is_pandigital(str(start_digits)[:9]):
            break
    index += 1
    first = second
    second = end_digits
    # Only the first and last 9 digits matter so we track them separately
    # end_digits tracks only the last 9
    end_digits = (first + second)%10**9
    # start_digits tracks the first 15 digits because extra precision is needed
    start_digits = int(start_digits*phi)
    if len(str(start_digits)) > 15:
        start_digits = int(str(start_digits)[:15])

end = time.time()

print(index)
print("Time taken: ", end-start, "s", sep="")
