"""""""""
# 소인수분해
"""""""""

n = int(input())

prime_num = [i for i in range(2, n+1) if not any([j for j in range(2, i) if i % j == 0])]
prime_factor = []

cnt = 0
while n > 1:
    prime = prime_num[cnt]
    print(prime_factor)
    if n % prime == 0:
        prime_factor.append(prime)
        n //= prime
        cnt = 0

    else:
        cnt += 1

for i in sorted(prime_factor):
    print(i)
