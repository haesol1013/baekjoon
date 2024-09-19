# 애너그램 만들기 - 1919

str1 = input()
str2 = input()
arr1 = [0] * 26
arr2 = [0] * 26

for i in str1:
    arr1[ord(i) - 97] += 1

for i in str2:
    arr2[ord(i) - 97] += 1

sum_ = 0
for i, j in zip(arr1, arr2):
    sum_ += abs(i - j)

print(sum_)
