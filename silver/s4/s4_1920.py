"""""""""
# 수 찾기
"""""""""

_ = int(input())
a = list(map(int, input().split()))

_ = int(input())
target = list(map(int, input().split()))

for x in target:
    print(1) if x in a else print(0)
