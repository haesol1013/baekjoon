# 프린터 큐 - 1966

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def printer(queue: deque, m: int) -> int:
    cnt = 1
    while True:
        curr_pair = queue.popleft()
        if not queue or curr_pair[1] >= max(queue, key=lambda x: x[1])[1]:
            if curr_pair[0] == m:
                return cnt
            cnt += 1
        else:
            queue.append(curr_pair)


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        queue = deque([(i, v) for i, v in enumerate(map(int, input().split()))])
        print(printer(queue, m))


if __name__ == "__main__":
    main()
