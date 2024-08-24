# N과 M (11) - 15665

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
arr = map(int, sys.stdin.readline().split())
for i in sorted(set(product(arr, repeat=m))):
    print(*i)
