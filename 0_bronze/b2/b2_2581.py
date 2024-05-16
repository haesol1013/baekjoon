# 소수 - 2581

start = int(input())
end = int(input())

prime_num = [i for i in range(start, end+1) if 2 == len([j for j in range(1, i+1) if i % j == 0])]

if len(prime_num) > 0:
    print(sum(prime_num))
    print(prime_num[0])
else:
    print(-1)
