# 포인트 카드 - 14471

import sys
input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
sum_ = [max(0, n - int(input().split()[0])) for _ in range(m)]
print(sum(sum_) - max(sum_))