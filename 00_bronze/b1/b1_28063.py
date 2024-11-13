# 동전 복사 - 28063

import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())
arr = [0] * (n+1)

for _ in range(n*(n-1) // 2):
    t1, t2, s1, s2 = map(int, input().split())
    if s1 > s2:
        arr[t1] += 3
    elif s1 < s2:
        arr[t2] += 3
    else:
        arr[t1] += 1
        arr[t2] += 1

rank_dict = dict()
rank = 1
for score in sorted(arr[1:], reverse=True):
    if score not in rank_dict:
        rank_dict[score] = rank
    rank += 1

for i in arr[1:]:
    print(rank_dict[i])