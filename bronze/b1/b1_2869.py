# 달팽이는 올라가고 싶다 - 2869

import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

day = (v-b) / (a-b)
print(math.ceil(day))
