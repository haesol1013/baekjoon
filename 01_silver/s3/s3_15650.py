# N과 M (2) - 15650

from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
for comb in combinations(range(1, n+1), m):
    print(*comb)
