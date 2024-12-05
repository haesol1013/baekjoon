# Triangle - 16509

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

def check(sides: list[int]) -> bool:
    return sides[0]**2 + sides[1]**2 == sides[2]**2


for _ in range(n):
    sides_1 = sorted(map(int, input().split()))
    sides_2 = sorted(map(int, input().split()))

    if sides_1 != sides_2:
        print('NO')
    elif not (check(sides_1) and check(sides_2)):
        print('NO')
    else:
        print('YES')
