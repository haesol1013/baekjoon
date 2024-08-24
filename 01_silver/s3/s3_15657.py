# N과 M (8) - 15657

import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for comb in combinations_with_replacement(arr, m):
    print(*comb)
