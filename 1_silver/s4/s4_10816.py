# 숫자 카드 2 - 10816

import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = input()
    existed_card = map(int, input().split())
    _ = input()
    targets = map(int, input().split())

    dict_ = dict()
    for card in existed_card:
        try:
            dict_[card] += 1
        except KeyError:
            dict_[card] = 1

    for target in targets:
        try:
            print(dict_[target], end=" ")
        except KeyError:
            print(0, end=" ")


main()
