# N과 M (7) - 15656

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for comb in product(arr, repeat=m):
    print(*comb)
