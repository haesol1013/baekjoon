# 나이순 정렬 - 10814

import sys

n = int(sys.stdin.readline())
user = [tuple(sys.stdin.readline().split()) for _ in range(n)]
user_new = list(map(lambda x: (int(x[0]), x[1]), user))
for i in sorted(user_new, key=lambda x: x[0]):
    print(*i)
