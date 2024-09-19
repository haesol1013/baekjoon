# Strfry - 11328

import sys
input = lambda: sys.stdin.readline().rstrip()


def can_make(target: str, ingrid: str) -> str:
    return "Possible" if sorted(target) == sorted(ingrid) else "Impossible"


n = int(input())
for _ in range(n):
    a, b = input().split()
    print(can_make(a, b))
