# 가로수 - 2485

def get_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def multiple_gcd(arr: list[int]) -> int:
    gcd: int = get_gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        gcd = get_gcd(gcd, arr[i])
    return gcd


def main():
    n = int(input())
    location = [int(input()) for _ in range(n)]
    diffs: list = []

    for i in range(1, n):
        diff = location[i] - location[i-1]
        diffs.append(diff)

    gcd: int = multiple_gcd(diffs)
    result: int = sum(map(lambda x: (x-gcd)//gcd, diffs))
    print(result)


main()
