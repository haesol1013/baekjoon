# 듣보잡 - 1764

import sys

n, m = map(int, sys.stdin.readline().split())
hear = {sys.stdin.readline().rstrip() for _ in range(n)}
see = {sys.stdin.readline().rstrip() for _ in range(m)}
hear_n_see = hear.intersection(see)

print(len(hear_n_see))
for element in sorted(hear_n_see):
    print(element)
