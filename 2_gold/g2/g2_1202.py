# 보석 도둑 - 1202

import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewel = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]
heapq.heapify(jewel)
total_value = 0
tmp_bag = []

for bag in sorted(bags):
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(tmp_bag, -heapq.heappop(jewel)[1])
    if tmp_bag:
        total_value -= heapq.heappop(tmp_bag)
    elif not jewel:
        break

print(total_value)
