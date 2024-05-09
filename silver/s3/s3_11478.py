# 서로 다른 부분 문자열의 개수 = 11478

from itertools import combinations
import sys

word = sys.stdin.readline().strip()

cnt = 0
for r in range(1, len(word)+1):
    for comb in combinations(word, r):
        cnt += 1
        print(*comb, cnt)
print(cnt)
