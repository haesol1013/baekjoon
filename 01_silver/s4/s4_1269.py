# 대칭 차집합

import sys

_ = sys.stdin.readline()
set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))
print(len(set_a.symmetric_difference(set_b)))
