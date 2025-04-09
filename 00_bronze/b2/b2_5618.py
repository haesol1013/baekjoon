# 공약수 - 5618

n = int(input())
nums = list(map(int, input().split()))
min_num = min(nums)
for i in range(1, min_num+1):
    cnt = 0
    for j in nums:
        if j % i == 0:
            cnt += 1
        else:
            break
    if n == cnt:
        print(i)
