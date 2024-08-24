# 소수 구하기 - 1929

m, n = map(int, input().split())
ni = [False, False] + [True]*(n-1)

for i, val in enumerate(ni):
    if val:
        if i >= m:
            print(i)
        for j in range(2*i, n+1, i):
            ni[j] = False
