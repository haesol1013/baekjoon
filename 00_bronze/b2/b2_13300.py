# 방 배정 - 13300

import sys
import math
input = lambda: sys.stdin.readline().rstrip()


n, k = map(int, input().split())
arr = [0] * 13

for _ in range(n):
    sex, grade = map(int, input().split())
    idx = grade if sex == 0 else grade + 6
    arr[idx] += 1

cnt = 0
for i in arr:
    cnt += math.ceil(i / k)
print(cnt)
