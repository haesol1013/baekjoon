# 노솔브 방지문제야!! - 15917

import sys
input = lambda: sys.stdin.readline().rstrip()


q = int(input())
for _ in range(q):
    a = int(input())
    if bin(a&-a) == bin(a):
        print(1)
    else:
        print(0)
