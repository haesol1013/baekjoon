# 삼각 무늬 - 1 - 11320

import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print((a//b) ** 2)