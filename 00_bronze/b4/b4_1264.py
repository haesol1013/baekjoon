# 모음의 개수 - 1264

import sys
input = lambda: sys.stdin.readline().rstrip()

vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}

while True:
    word = input()
    if word == '#':
        break
    cnt = 0
    for i in word:
        if i in vowels:
            cnt += 1
    print(cnt)