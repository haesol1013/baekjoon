# 민균이의 비밀번호 - 9933

import sys
input = lambda: sys.stdin.readline().rstrip()


def print_ans(word: str) -> None:
    len_s = len(word)
    print(len_s, word[len_s//2])


n = int(input())
set_ = set()
for _ in range(n):
    s = input()
    reversed_s = "".join(reversed(s))
    if s == reversed_s:
        print_ans(s)
        break
    elif reversed_s in set_:
        print_ans(s)
        break
    else:
        set_.add(s)
