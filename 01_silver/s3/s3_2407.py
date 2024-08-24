# 조합 - 2407

import math

n, m = map(int, input().split())
result = math.perm(n, m) // math.factorial(m)
print(result)
