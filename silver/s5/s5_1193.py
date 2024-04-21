"""""""""
# 분수 찾기
"""""""""


def find_frac(n: int) -> str:
    line = 0
    card = 0
    while card < n:
        line += 1
        card += line

    pre_card = card - line
    if line % 2 == 0:
        x = n - pre_card
        y = card - n + 1
    else:
        x = card - n + 1
        y = n - pre_card

    return str(x) + '/' + str(y)


n = int(input())
print(find_frac(n))
