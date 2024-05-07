# 회사에 있는 사람 - 7785

import sys

n = int(sys.stdin.readline())
mem = []
for _ in range(n):
    name, order = sys.stdin.readline().strip().split()
    match order:
        case "enter":
            mem.append(name)
        case "leave":
            mem.remove(name)

for i in sorted(mem, reverse=True):
    print(i)
