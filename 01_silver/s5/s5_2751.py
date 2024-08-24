# 수 정렬하기 - 2751

import sys


n = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(num_list):
    print(num)
