# N과 M (4) - 15652

from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().split())
for comb in combinations_with_replacement(range(1, n+1), m):
    print(*comb)
