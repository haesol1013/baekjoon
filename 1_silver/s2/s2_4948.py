# 베르트랑 공준 - 4948


def get_prime_num(n):
    ni = [False, False] + [True]*(2*n-1)
    cnt = 0

    for i, val in enumerate(ni):
        if val:
            if n < i <= 2*n:
                cnt += 1

            for j in range(2*i, 2*n+1, i):
                ni[j] = False

    return cnt


while True:
    n = int(input())
    if n == 0:
        break
    print(get_prime_num(n))
