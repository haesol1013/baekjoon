# 설탕 배탈 - 2839


def get_sugars(n: int) -> int:
    result = 0
    while n > -1:
        if n % 5 == 0:
            result += n // 5
            return result
        n -= 3
        result += 1
    else:
        return -1


def main():
    n = int(input())
    print(get_sugars(n))


main()
