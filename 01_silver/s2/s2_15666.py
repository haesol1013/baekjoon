# N과 M (12) - 15666

import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for comb in sorted(set(combinations_with_replacement(arr, m))):
    print(*comb)
