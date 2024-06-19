# 괄호 - 9012

import sys


t = int(sys.stdin.readline())


def checker(target: str):
    arr = []
    for chr_ in target:
        if chr_ == '(':
            arr.append(chr_)
        else:
            if not arr:
                arr.append(chr_)
            elif arr[-1] == '(':
                arr.pop()
            else:
                arr.append(chr_)
    result = "NO" if arr else "YES"
    return result


for _ in range(t):
    paren = sys.stdin.readline().rstrip()
    print(checker(paren))
