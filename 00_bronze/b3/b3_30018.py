# 타슈 - 30018

_ = int(input())
a = map(int, input().split())
b = map(int, input().split())

cnt = 0
for i, j in zip(a, b):
    if i > j:
        cnt += i - j
print(cnt)
