# k번째 수 - 11004

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(sorted(arr)[k-1])
