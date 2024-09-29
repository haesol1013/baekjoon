# ANA는 회문이야 - 32401

_ = input()
s = input()
arr = s.split("A")

cnt = 0
for i in arr[1:-1]:
    if i.count("N") == 1: cnt += 1
print(cnt)
