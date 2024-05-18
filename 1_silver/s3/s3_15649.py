# N과 M (1) - 15649

from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
for permutation in permutations(range(1, n+1), m):
    print(*permutation)
