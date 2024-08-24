# N과 M (10) - 15664

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for comb in sorted(set(combinations(arr, m))):
    print(*comb)
