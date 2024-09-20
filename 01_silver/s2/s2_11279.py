# 최대 힙 - 11279

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


n = int(input())
max_heap = []

for _ in range(n):
     x = int(input())
     if x:
         heapq.heappush(max_heap, -x)
     else:
         result = -heapq.heappop(max_heap) if max_heap else 0
         print(result)
