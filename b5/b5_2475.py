a, b, c, d, e = map(int, input().split())


def verify(n1, n2, n3, n4, n5):
    square = n1 ** 2 + n2 ** 2 + n3 ** 2 + n4 ** 2 + n5 ** 2
    result = square % 10
    return result


print(verify(a, b, c, d, e))
