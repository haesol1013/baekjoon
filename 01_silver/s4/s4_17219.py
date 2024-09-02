# 비밀번호 찾기 - 17219

import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    
    dict_ = dict()
    for _ in range(n):
        key, val = input().split()
        dict_[key] = val
    
    for _ in range(m):
        target = input()
        print(dict_[target])


main()
