# 별 찍기 - 17 - 10992

n = int(input())
print(" "*(n-1) + "*")
if n > 2:
    a = n-1
    for i in range(1, a):
        print(" "*(a-i) + "*" + " "*(2*i - 1) + "*")
if n > 1:
    print("*"*(2*n - 1))
