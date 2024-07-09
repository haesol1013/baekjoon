# 홀수 - 2576

import sys

arr = [int(sys.stdin.readline()) for _ in range(7)]
odd_arr = [i for i in arr if i % 2 != 0]
if odd_arr:
    print(sum(odd_arr))
    print(min(odd_arr))
else:
    print(-1)
