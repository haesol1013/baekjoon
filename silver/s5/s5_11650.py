"""""""""
# 좌표 정렬하기
"""""""""

n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
for pair in sorted(pos):
    print(*pair)
