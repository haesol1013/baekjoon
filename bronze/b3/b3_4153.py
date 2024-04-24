"""""""""
# 직각삼각형
"""""""""

while True:
    side = list(map(int, input().split()))

    if side.count(0) == 3:
        break

    max_s = side.pop(side.index(max(side)))
    is_rat = max_s ** 2 == sum([x**2 for x in side])
    result = "right" if is_rat else "wrong"
    print(result)
