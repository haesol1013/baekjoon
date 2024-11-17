# Civil Engineering - 5287

import sys

input = lambda: sys.stdin.readline()


def print_ans(dataset_num: int):
    n, m = map(int, input().split())
    density = [int(input()) for _ in range(n)]

    total_weight = 0
    for _ in range(m):
        h, w, d, i = map(int, input().split())
        total_weight += h * w * d * density[i-1]

    print(f"Data Set {dataset_num+1}:")
    print(total_weight)


k = int(input())
for i in range(k):
    print_ans(i)
