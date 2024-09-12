# 최소 힙 - 1927

import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    heap = []

    for _ in range(n):
        x = int(input())
        if x:
            heapq.heappush(heap, x)
        else:
            min_ = heapq.heappop(heap) if heap else 0
            print(min_)


if __name__ == "__main__":
    main()
