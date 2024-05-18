# 싱기한 네자리 숫자 - 6679


def checker(n, d):
    sum_ = 0
    while n > 0:
        sum_ += n % d
        n //= d
    return sum_


for i in range(2992, 10000):
    if checker(i, 10) == checker(i, 12) == checker(i, 16):
        print(i)


