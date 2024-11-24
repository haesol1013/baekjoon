# 아이 러브 크로아티아 - 9517

import sys
input = lambda: sys.stdin.readline().rstrip()


k = int(input()) - 1
n = int(input())

curr_time = 0
for _ in range(n):
    t, z = input().split()
    curr_time += int(t)
    if curr_time >= 210:
        break
    if z == "T":
        k = (k+1) % 8
print(k + 1)
