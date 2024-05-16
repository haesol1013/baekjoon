# 숫자 카드 - 10815

import sys

_ = sys.stdin.readline()
std_card = set(map(int, sys.stdin.readline().split()))
_ = sys.stdin.readline()
check_card = list(map(int, sys.stdin.readline().split()))

for card in check_card:
    print(1, end=" ") if card in std_card else print(0, end=" ")
