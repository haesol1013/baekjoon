# Axis-Aligned Area - 30596

import sys
input = lambda: sys.stdin.readline().rstrip()

arr = [int(input()) for _ in range(4)]

print(min(arr[0], arr[1]) * min(arr[2], arr[3]))
