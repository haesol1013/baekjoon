# 큐 2 - 18258

import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    order = sys.stdin.readline().strip().split()
    match order[0]:
        case "push":
            arr.append(order[1])
        case "pop":
            print(arr.pop(0)) if arr else print(-1)
        case "size":
            print(len(arr))
        case "empty":
            print(0) if arr else print(1)
        case "front":
            print(arr[0]) if arr else print(-1)
        case "back":
            print(arr[-1]) if arr else print(-1)
            