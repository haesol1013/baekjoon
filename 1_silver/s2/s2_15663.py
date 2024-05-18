# N과 M (9) - 15663

import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = map(int, sys.stdin.readline().split())
for i in sorted(set(permutations(arr, m))):
    print(*i)
