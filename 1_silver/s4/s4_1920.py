# 수 찾기 - 1920

_ = int(input())
n = set(map(int, input().split()))

_ = int(input())
target = list(map(int, input().split()))

for x in target:
    print(1) if x in n else print(0)
