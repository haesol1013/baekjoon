"""""""""
# 직사각형에서 탈출
"""""""""

x, y, w, h = map(int, input().split())
min_x = min(x, w-x)
min_y = min(y, h-y)
result = min(min_x, min_y)
print(result)
