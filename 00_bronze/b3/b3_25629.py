# 홀짝 수열 - 25629

n = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(1 if even == n // 2 and odd == n//2 + n % 2 else 0)
