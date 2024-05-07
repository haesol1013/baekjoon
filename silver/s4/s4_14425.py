# 문자열 집합 - 14425

import sys

n, m = map(int, sys.stdin.readline().split())
std_set = {sys.stdin.readline().strip() for _ in range(n)}
cnt = 0

for i in range(m):
    if sys.stdin.readline().strip() in std_set:
        cnt += 1

print(cnt)
