# 최소공배수 - 13241

import sys

a, b = map(int, sys.stdin.readline().split())
multiple = a*b
while a % b != 0:
    a, b = b, a % b
print(multiple//b)
