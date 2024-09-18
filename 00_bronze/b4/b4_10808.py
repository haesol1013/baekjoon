# 알파벳 개수 - 10808

words = input()
arr = [0] * 26
for word in words:
    arr[ord(word)-97] += 1
print(*arr)
