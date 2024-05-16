# 재귀의 귀재 - 25501

import sys


def checker(word: str, cnt=0):
    cnt += 1
    if len(word) < 2:
        return 1, cnt
    else:
        if word[0] == word[-1]:
            return checker(word[1:-1], cnt)
        else:
            return 0, cnt


n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(*checker(word))
