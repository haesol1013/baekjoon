# 별 찍기 - 9 - 2446

n = int(input())
for i in range(n, 1, -1):
    print(" "*(n-i) + "*"*(2*i - 1))
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i - 1))
