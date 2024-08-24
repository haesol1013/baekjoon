# 이항 계수 2 - 11051

import math

n, m = map(int, input().split())
result = math.perm(n, m) // math.factorial(m) % 10007
print(result)
