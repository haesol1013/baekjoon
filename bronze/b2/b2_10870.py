# 피보나치수 5 - 10870

def fibo(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))
