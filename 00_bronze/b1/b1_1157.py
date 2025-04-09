# 단어 공부 - 1157

s = input().upper()
set_s = list(set(s))
nums = [s.count(i) for i in set_s]
max_ = max(nums)
if nums.count(max_) == 1:
    print(set_s[nums.index(max_)])
else:
    print("?")