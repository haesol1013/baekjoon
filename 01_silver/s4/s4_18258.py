# 큐 2 - 18258

import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    arr = deque()

    for _ in range(n):
        order = sys.stdin.readline().strip().split()
        match order[0]:
            case "push":
                arr.append(order[1])
            case "pop":
                print(arr.popleft()) if arr else print(-1)
            case "size":
                print(len(arr))
            case "empty":
                print(1) if not arr else print(0)
            case "front":
                print(arr[0]) if arr else print(-1)
            case "back":
                print(arr[-1]) if arr else print(-1)
            case _:
                continue


main()
