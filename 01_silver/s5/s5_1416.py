# 국회의원 선거 - 1416

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


n = int(input())
standard = int(input())

enemy = []
for _ in range(n-1):
    heapq.heappush(enemy, -int(input()))

cnt = 0
if enemy:
    while standard <= -enemy[0]:
        max_num = heapq.heappop(enemy)
        cnt += 1; standard += 1; max_num += 1
        heapq.heappush(enemy, max_num)

print(cnt)
