"""""""""
# 수 정렬하기
"""""""""

import sys


n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
for i in sorted(num):
    print(i)
