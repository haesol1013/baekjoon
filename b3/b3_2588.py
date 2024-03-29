num1 = int(input())
num2 = int(input())

num2_digit3 = num2 // 100
num2_digit2 = num2 % 100 // 10
num2_digit1 = num2 % 100 % 10
result = (num1 * num2_digit3 * 10**2) + (num1 * num2_digit2 * 10) + (num1 * num2_digit1)

print(num1 * num2_digit1)
print(num1 * num2_digit2)
print(num1 * num2_digit3)
print(result)