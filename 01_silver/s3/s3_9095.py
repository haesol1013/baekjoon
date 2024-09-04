# 1, 2, 3 더하기 - 9095

import sys
input = lambda: sys.stdin.readline().rstrip()


def comb(n: int, curr_sum: int = 0) -> int:
    if n == curr_sum:
        return 1
    elif n < curr_sum:
        return 0

    cnt = 0
    for i in range(1, 4):
        cnt += comb(n, curr_sum+i)
    return cnt


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(comb(n))


if __name__ == "__main__":
    main()
