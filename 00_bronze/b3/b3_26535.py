# Chicken Pen - 26535

import math

n = int(input())
repeat = math.ceil(n**0.5) + 2

for i in range(repeat):
    if i == 0 or i == repeat-1:
        print("x"*repeat)
    else:
        print("x" + "."*(repeat-2) + "x")
