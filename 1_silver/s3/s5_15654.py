# N과 M (5) - 15654

import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for i in permutations(arr, m):
    print(*i)
