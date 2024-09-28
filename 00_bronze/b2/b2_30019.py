# 강의실 예약 시스템 - 30019

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [0] * (n+1)

for _ in range(m):
    room, s, e = map(int, input().split())
    if arr[room] <= s:
        print("YES")
        arr[room] = e
    else:
        print("NO")
