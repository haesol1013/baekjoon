"""""""""
# 팩토리얼 2
"""""""""


def fact(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


n = int(input())
print(fact(n))
