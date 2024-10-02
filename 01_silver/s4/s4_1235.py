# 학생 번호 - 1235

import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())
arr = [input() for _ in range(n)]

ans = 1
for i in range(len(arr[0])-1, 0, -1):
    set_ = set()
    for s in arr:
        set_.add(s[i:])
    if n == len(set_):
        break
    ans += 1
print(ans)

