"""""""""
# 단어 뒤집기
"""""""""

n = int(input())

for _ in range(n):
    sentence = input().split()
    rev_sentence = map(''.join, map(reversed, sentence))
    print(*rev_sentence)
