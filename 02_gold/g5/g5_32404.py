# 일이 커졌어 - 32404

n = int(input())
big = list(range(n, n//2, -1))
small = list(range(1, n//2+1))

for i in range(1, n+1):
    if i % 2 != 0: print(big.pop(), end=" ")
    else: print(small.pop(), end=" ")
