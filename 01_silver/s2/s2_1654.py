# 랜선 자르기 - 1654

import sys
input = lambda: sys.stdin.readline().rstrip()


def count_lan(lan_list: list[int], length: int) -> int:
    return sum(lan // length for lan in lan_list)


def binary_search(lan_list: list[int], n: int) -> int:
    start, end = 1, max(lan_list)
    while start <= end:
        mid = (start + end) // 2
        if count_lan(lan_list, mid) >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end


def main():
    k, n = map(int, input().split())
    lan_list = [int(input()) for _ in range(k)]
    print(binary_search(lan_list, n))


if __name__ == "__main__":
    main()
