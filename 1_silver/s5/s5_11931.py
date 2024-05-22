# 수 정렬하기 4

import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
for i in sorted(arr, reverse=True):
    print(i)
