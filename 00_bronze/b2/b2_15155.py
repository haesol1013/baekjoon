# Analysis of Advanced Analytics - 15155

import sys
input = lambda: sys.stdin.readline().rstrip()


n, k = map(int, input().split())
needed = list(map(int, input().split()))

used = needed[0]
cnt = 1
for i in range(1, n):
    used += needed[i]
    if used > k:
        cnt += 1
        used = needed[i]
print(cnt)
