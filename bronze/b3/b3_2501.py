n, k = map(int, input().split())

divisor = [num for num in range(1, n+1) if n % num == 0]
result = divisor[k-1] if len(divisor) >= k else 0
print(result)
