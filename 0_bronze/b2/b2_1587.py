# 대표값2 - 1587

import sys

num = [int(sys.stdin.readline()) for _ in range(5)]
print(sum(num) // len(num))
print(sorted(num)[len(num)//2])
