# 공 넣기 - 10810

import sys

n, m = map(int, sys.stdin.readline().split())
box = [0]*n
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    box[i-1:j] = [k]*(j-i+1)
print(*box)
