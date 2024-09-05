# 통계학 - 2108

import sys
input = lambda: sys.stdin.readline().rstrip()


def get_mean(arr: list[int]) -> int:
    return round(sum(arr) / len(arr))


def get_median(arr: list[int]) -> int:
    return arr[int(len(arr)/2)]


def get_mode(arr: list[int]) -> int:
    info: list[tuple[int, int]] = [(i, arr.count(i)) for i in set(arr)]
    info.sort(key=lambda x: (-x[1], x[0]))
    if len(info) > 1 and info[0][1] == info[1][1]:
        return info[1][0]
    else:
        return info[0][0]


def get_diff(arr: list[int]) -> int:
    return arr[-1] - arr[0]


def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    print(get_mean(arr))
    print(get_median(arr))
    print(get_mode(arr))
    print(get_diff(arr))


if __name__ == "__main__":
    main()