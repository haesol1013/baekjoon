num1, num2 = input().split()
num1 = int(''.join(reversed(num1)))
num2 = int(''.join(reversed(num2)))

print(max(num1, num2))
