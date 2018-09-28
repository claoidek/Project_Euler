# Calculates the maximum value path from the top to the bottom of the following triangle
#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

import time
import math

start = time.clock()

triangle = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20,  4, 82, 47, 65, 19,  1, 23, 75,  3, 34, 88,  2, 77, 73,  7, 63, 67, 99, 65,  4, 28,  6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,  4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]

# Inverse of the formula for triangular numbers:
# T_n = n*(n+1)/2
num_rows = int(0.5*(math.sqrt(8*len(triangle)+1)-1))

# Cycles through the numbers and increases them by the largest of their two
# upper neighbours. This effectively replaces each number in the triangle by
# the maximum value a path can take that ends at that number. Then all we need
# to do is find the maximuim value on the last row.
for i in range(1,num_rows):
    triangle[i*(i+1)/2] += triangle[i*(i-1)/2]
    for j in range(1,i):
        triangle[i*(i+1)/2+j] += max(triangle[i*(i-1)/2+j],triangle[i*(i-1)/2+j-1])
    triangle[i*(i+1)/2+i] = triangle[i*(i-1)/2+i-1] + triangle[i*(i+1)/2+i]

end = time.clock()

print max(triangle[-num_rows:])
print "Time taken: ", end-start, " s"
