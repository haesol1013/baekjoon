# 팰린드롬 소떡소떡 - 25630

n = int(input())
str_ = input()

cnt = 0
for i in range(n//2):
    if str_[i] != str_[-i-1]:
        cnt += 1
print(cnt)

