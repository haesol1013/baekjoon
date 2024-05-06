# 팰린드롬 수 - 1259

while True:
    n = int(input())

    if n == 0:
        break
    else:
        n = str(n)
        print("yes") if list(n) == list(reversed(n)) else print("no")
