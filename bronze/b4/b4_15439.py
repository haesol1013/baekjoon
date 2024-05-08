# 베라의 패션 - 15439

from math import factorial

n = int(input())
if n >= 2:
    print(factorial(n)//factorial(n-2))
else:
    print(0)
