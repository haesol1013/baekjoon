# 플래피 버드 스코어링 - 26152

import sys
input = sys.stdin.readline

_ = int(input())
top = tuple(map(int, input().split()))
bottom = tuple(map(int, input().split()))
_ = int(input())
bird_sizes = tuple(map(int, input().split()))
terms = [x[0] - x[1] for x in zip(top, bottom)]

scores = []
for bird_size in bird_sizes:
    score = 0
    for term in terms:
        if bird_size > term:
            break
        else:
            score += 1
    scores.append(score)

for score in scores:
    print(score)
