"""""""""
# 커트라인
"""""""""

n, k = map(int, input().split())
num = sorted(map(int, input().split()))
print(num[-k])