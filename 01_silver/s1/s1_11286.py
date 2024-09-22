# 절댓값 힙 - 11286

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


n = int(input())
abs_heap = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(abs_heap, (abs(x), 1 if x >= 0 else -1))
    else:
        tmp = heapq.heappop(abs_heap) if abs_heap else (0, 0)
        print(tmp[0] * tmp[1])
