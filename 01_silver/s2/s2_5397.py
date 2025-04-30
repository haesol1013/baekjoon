# 키로거 - 5397

import sys
input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    s = input()
    l = []
    r = []
    for char in s:
        match char:
            case "<":
                if l:
                    r.append(l.pop())
            case ">":
                if r:
                    l.append(r.pop())
            case "-":
                if l:
                    l.pop()
            case _:
                l.append(char)
    print("".join(l + list(reversed(r))))
