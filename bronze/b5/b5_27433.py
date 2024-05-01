"""""""""
# 팩토리얼 2
"""""""""


def fact(n: int) -> int:
    if n > 0:
        return fact(n-1) * n
    else:
        return 1


n = int(input())
print(fact(n))
