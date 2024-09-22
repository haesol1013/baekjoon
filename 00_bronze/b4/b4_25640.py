# MBTI - 25640

jinho = input()
n = int(input())
arr = [input() for _ in range(n)]

cnt = 0
for i in arr:
    if i == jinho:
        cnt += 1
print(cnt)
