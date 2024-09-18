# 두 수의 합 - 3273

import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

cnt = 0
start, end = 0, n-1

while start < end:
    sum_ = arr[start] + arr[end]
    if sum_ == x:
        cnt += 1
        start += 1
        end -= 1
    elif sum_ < x:
        start += 1
    else:
        end -= 1

print(cnt)
