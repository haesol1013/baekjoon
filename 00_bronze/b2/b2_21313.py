# 문어 - 21313

n = int(input())

for i in range(1, n+1):
    if i % 2:
        if n == i:
            print(3, end=" ")
        else:
            print(1, end=" ")
    else:
        print(2, end=" ")
