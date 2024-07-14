# 팩토리얼 0의 개수 - 1676

import sys
import math

n = int(sys.stdin.readline())
cnt = 0
for i in reversed(str(math.factorial(n))):
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)
