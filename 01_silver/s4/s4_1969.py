# DNA - 1969

import sys
input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = [input() for _ in range(n)]

ans = []
sum_ = 0
for j in range(m):
    a, c, g, t = [0] * 4

    for i in range(n):
        s = arr[i][j]
        if s == "A":
            a += 1
        elif s == "C":
            c += 1
        elif s == "G":
            g += 1
        elif s == "T":
            t += 1

    max_ = max(a, c, g, t)
    if a == max_:
        ans.append("A")
    elif c == max_:
        ans.append("C")
    elif g == max_:
        ans.append("G")
    elif t == max_:
        ans.append("T")

    sum_ += n - max_

print("".join(ans))
print(sum_)
