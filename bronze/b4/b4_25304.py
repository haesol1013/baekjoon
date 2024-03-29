X = int(input())
N = int(input())
sum_ = 0

for i in range(N):
    a, b = map(int, input().split())
    sum_ += a * b

result = "Yes" if sum_ == X else "No"
print(result)
