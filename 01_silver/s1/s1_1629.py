# 곱셈 - 1629


def power(x, y, z):
    result = 1
    while y > 0:
        if y % 2 != 0:
            result = result * x % z
        y //= 2
        x = (x * x) % z
    return result


a, b, c = map(int, input().split())
print(power(a, b, c))
