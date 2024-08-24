# 윷놀이 - 2490

import sys

for _ in range(3):
    sum_ = sum(map(int, sys.stdin.readline().split()))
    match sum_:
        case 0:
            print("D")
        case 1:
            print("C")
        case 2:
            print("B")
        case 3:
            print("A")
        case 4:
            print("E")
