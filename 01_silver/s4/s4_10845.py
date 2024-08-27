# 큐 - 10845

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    queue = deque()

    for _ in range(n):
        order = input().split()
        match order[0]:
            case "push":
                queue.append(int(order[1]))
            case "pop":
                print(queue.popleft()) if queue else print(-1)
            case "size":
                print(len(queue))
            case "empty":
                print(1) if not queue else print(0)
            case "front":
                print(queue[0]) if queue else print(-1)
            case "back":
                print(queue[-1]) if queue else print(-1)
            case _:
                continue


main()
