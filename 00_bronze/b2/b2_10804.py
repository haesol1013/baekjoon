# 카드 역배치 - 10804

import sys
input = lambda: sys.stdin.readline().rstrip()


arr = list(range(21))
for _ in range(10):
    s,e = map(int, input().split())
    arr[s:e+1] = reversed(arr[s:e+1])
print(*arr[1:])
