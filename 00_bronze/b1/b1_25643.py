# 문자열 탑 쌓기 - 25643

n, m = map(int, input().split())
arr = [input() for _ in range(n)]


def can_make(arr, n, m):
    for i in range(n-1):
        x, y = arr[i], arr[i+1]

        match = False
        for j in range(1, m+1):
            if x[m-j:] == y[:j]:
                match = True
                break

        if not match:
            for j in range(1, m):
                if x[:m-j] == y[j:]:
                    match = True
                    break

        if not match:
            return 0
    return 1


print(can_make(arr, n, m))
