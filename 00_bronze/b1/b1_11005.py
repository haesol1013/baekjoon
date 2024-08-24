n, b = map(int, input().split())
digit = []
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n > 0:
    remainder = n % b
    n //= b
    digit.append(num[remainder])

print(''.join(reversed(digit)))
