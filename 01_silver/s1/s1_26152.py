# 플래피 버드 스코어링 - 26152

import sys
input = lambda: sys.stdin.readline().rstrip()


def binary_search(arr: list[int], bird: int, length: int) -> int:
    if arr[0] < bird:
        return 0

    start, end = 1, length - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < bird:
            end = mid - 1
        else:
            start = mid + 1
    return start


def main():
    n = int(input())
    top = tuple(map(int, input().split()))
    bottom = tuple(map(int, input().split()))
    _ = int(input())
    bird_sizes = tuple(map(int, input().split()))

    limits = [0] * n
    min_val = 10**19
    for i in range(n):
        min_val = min(top[i] - bottom[i], min_val)
        limits[i] = min_val

    for bird in bird_sizes:
        print(binary_search(limits, bird, n))


main()
