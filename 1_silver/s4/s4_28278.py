# 스택 2 - 28278

import sys

arr = []
n = int(sys.stdin.readline())

for _ in range(n):
    str_ = sys.stdin.readline().strip()
    x = 0
    try:
        order = int(str_)
    except ValueError:
        order, x = map(int, str_.split())

    match order:
        case 1:
            arr.append(x)
        case 2:
            print(arr.pop()) if arr else print(-1)
        case 3:
            print(len(arr))
        case 4:
            print(0) if arr else print(1)
        case 5:
            print(arr[-1]) if arr else print(-1)
