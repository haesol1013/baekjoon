"""""""""
# 단어 정렬
"""""""""

import sys


n = int(sys.stdin.readline())
word = set([sys.stdin.readline().strip() for _ in range(n)])
for i in sorted(word, key=lambda x: (len(x), x)):
    print(i)

