"""""""""
# 이항 계수 1
"""""""""


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


n, k = map(int, input().split())
result = factorial(n) // factorial(n-k) // factorial(k)
print(result)
