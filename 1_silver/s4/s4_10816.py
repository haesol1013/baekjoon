# 숫자 카드 2 - 10816

import sys
import numpy as np

_ = sys.stdin.readline()
std_list = list(map(int, sys.stdin.readline().split()))
std_set = set(std_list)
_ = sys.stdin.readline()
check_card = list(map(int, sys.stdin.readline().split()))

for card in check_card:
    if card in std_set:
        cnt = std_list.count(card)
        print(cnt, end=" ")

        std_set.remove(card)
        for _ in range(cnt):
            std_list.remove(card)

    else:
        print(0, end=" ")
