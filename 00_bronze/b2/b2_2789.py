# 블랙잭 - 2798

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
high_comb = 0

for comb in combinations(arr, 3):
    if high_comb < sum(comb) <= m:
        high_comb = sum(comb)

print(high_comb)
