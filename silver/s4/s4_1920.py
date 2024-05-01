"""""""""
# 수 찾기
"""""""""

_ = int(input())
n = list(map(int, input().split()))

_ = int(input())
target = list(map(int, input().split()))

for x in target:
    print(1) if x in n else print(0)
