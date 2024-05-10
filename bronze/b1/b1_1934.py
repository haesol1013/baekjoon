# 최소공배수 - 1934

import sys


def lcm(n1: int, n2: int) -> int:
    gcd = 1
    for i in range(min(n1, n2), 1, -1):
        if n1 % i + n2 % i == 0:
            gcd = i
            break
    return n1 * n2 // gcd


n = int(sys.stdin.readline())
for _ in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(lcm(n1, n2))
