H, M = map(int, input().split())
C = int(input())
M += C

while H > 23 or M > 59:
    if M > 59:
        M -= 60
        H += 1

    if H > 23:
        H -= 24

print(H, M)
