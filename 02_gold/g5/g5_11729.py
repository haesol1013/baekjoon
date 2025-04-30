# 하노이 탑 이동 순서 - 11729

def hanoi(n, start=1, mid=2, end=3):
    if n == 0:
        return
    hanoi(n-1, start, end, mid)
    print(start, end)
    hanoi(n-1, mid, start, end)


n = int(input())
print(2**n - 1)
hanoi(n)
