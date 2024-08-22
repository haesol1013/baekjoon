# 구간 합 구하기 - 11659

import sys
input = lambda: sys.stdin.readline().rstrip()


def get_prefix_sum_list(arr: list[int]) -> list[int]:
    prefix = [0]
    sum_ = 0

    for i in arr:
        sum_ += i
        prefix.append(sum_)

    return prefix


def get_sum(prefix: list[int], start: int, end: int) -> int:
    sum_ = prefix[end] - prefix[start-1]
    return sum_


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = get_prefix_sum_list(arr)

    for _ in range(m):
        i, j = map(int, input().split())
        print(get_sum(prefix, i, j))


main()
