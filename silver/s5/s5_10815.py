"""""""""
# 숫자 카드
"""""""""

import sys

_ = int(input())
card_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
check_list = list(map(int, sys.stdin.readline().split()))
result = [0] * m

for index, x in enumerate(check_list):
    if x in card_list:
        result[index] = 1

print(*result)
