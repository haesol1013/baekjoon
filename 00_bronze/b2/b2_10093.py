# 숫자 - 10093

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

print(max(0, b - a - 1))
print(*range(a + 1, b))
