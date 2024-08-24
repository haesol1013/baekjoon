"""""""""
# 최대공약수와 최소공배수
"""""""""

a, b = map(int, input().split())

gcd = 1
for x in range(min(a, b), 1, -1):
    if a % x == 0 and b % x == 0:
        gcd = x
        break

i = max(a, b)
lcm = i
while True:
    if i % a == 0 and i % b == 0:
        lcm = i
        break
    else:
        i += 1

print(gcd)
print(lcm)
