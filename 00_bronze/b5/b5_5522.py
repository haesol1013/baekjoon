# 5522 - 카드 게임

import sys
input = lambda: sys.stdin.readline()

score = 0
for _ in range(5):
    score += int(input())
print(score)
