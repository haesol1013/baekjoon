# 핸드폰 요금 - 1267

import sys
input = lambda: sys.stdin.readline().rstrip()


def get_cheaper(times: list[int]) -> str:
    y = sum(map(lambda x: (x//30 + 1) * 10, times))
    m = sum(map(lambda x: (x//60 + 1) * 15, times))

    if y == m:
        return f"Y M {y}"
    elif y > m:
        return f"M {m}"
    else:
        return f"Y {y}"


def main():
    _ = int(input())
    times = list(map(int, input().split()))
    print(get_cheaper(times))


main()
