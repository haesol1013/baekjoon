# 동전 0 - 11047

import sys

n, k = map(int, input().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
# coin = [int(sys.stdin.readline()) for i in range(n) if i >= k]
cnt = 0
for value in reversed(coin):
    cnt += k // value
    k = k % value
    if k == 0:
        break
print(cnt)
