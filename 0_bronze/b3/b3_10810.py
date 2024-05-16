# 공 넣기 - 10810

import sys

n, k = map(int, sys.stdin.readline().split())
box = [0]*n
for _ in range(4):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i-1, j):
        box[x] = k
print(*box)
