# 덱 2 - 28279

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    queue = deque()

    for _ in range(n):
        order = input().split()

        match int(order[0]):
            case 1:
                queue.appendleft(int(order[1]))
            case 2:
                queue.append(int(order[1]))
            case 3:
                print(queue.popleft()) if queue else print(-1)
            case 4:
                print(queue.pop()) if queue else print(-1)
            case 5:
                print(len(queue))
            case 6:
                print(1) if not queue else print(0)
            case 7:
                print(queue[0]) if queue else print(-1)
            case 8:
                print(queue[-1]) if queue else print(-1)
            case _:
                continue


main()
