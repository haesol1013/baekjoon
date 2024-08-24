# N과 M (6) - 15655

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for comb in combinations(arr, m):
    print(*comb)
