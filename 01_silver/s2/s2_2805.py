# 나무 자르기 - 2805

import sys
input = lambda: sys.stdin.readline().rstrip()


def binary_search(trees: list[int], m: int) -> int:
    start, end = 1, max(trees)
    while start <= end:
        mid = (start + end) // 2
        if get_trees(trees, mid) >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


def get_trees(trees: list[int], height: int) -> int:
    return sum(tree - height for tree in trees if tree - height > 0)


def main():
    _, m = map(int, input().split())
    trees = list(map(int, input().split()))
    print(binary_search(trees, m))


if __name__ == "__main__":
    main()
