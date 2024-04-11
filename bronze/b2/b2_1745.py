n, b = input().split()
n = ''.join(reversed(n))
b = int(b)

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
summation = 0

for digit in range(len(n)):
    summation += num.index(n[digit]) * b**digit

print(summation)
