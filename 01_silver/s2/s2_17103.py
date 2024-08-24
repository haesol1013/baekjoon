# 골드바흐 파티션 - 17103

def get_primes(n: int) -> tuple[list[int], list[bool]]:
    check = [False, False] + [True]*(n-1)
    primes = []
    for i, val in enumerate(check):
        if val:
            primes.append(i)
            for j in range(i*i, n+1, i):
                check[j] = False
    return primes, check


def get_gb(n) -> int:
    cnt = 0
    primes, check = get_primes(10**6)
    for i in primes:
        if i > n:
            break
        if check[n-i] and i <= n-i:
            cnt += 1
    return cnt


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = get_gb(n)
        print(result)


main()
