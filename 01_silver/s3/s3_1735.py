# 분수 합 - 1735

import sys


def gcd(a: int, b: int) -> int:
    a, b = (a, b) if a >= b else (b, a)
    while a % b != 0:
        a, b = b, a % b
    return b


a1, b1, = map(int, sys.stdin.readline().split())
a2, b2, = map(int, sys.stdin.readline().split())
numerator = a1*b2 + a2*b1
denominator = b1*b2
gcd_ = gcd(numerator, denominator)
print(numerator//gcd_, denominator//gcd_)
