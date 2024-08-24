# 다음 소수 - 4134

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            return
        else:
            n += 1


t = int(input())
for i in range(t):
    main()
