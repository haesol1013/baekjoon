# 주사위 세개 - 2480

arr = list(map(int, input().split()))
d1, d2, d3 = sorted(arr)

if d1 == d2 == d3:
    print(10000 + d3*1000)
elif d1 != d2 != d3:
    print(d3*100)
else:
    print(1000 + d2*100)
