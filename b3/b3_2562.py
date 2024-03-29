import sys


lst = [int(sys.stdin.readline()) for _ in range(9)]
max_ = 0

for i in range(9):
    if lst[i] > max_:
        max_ = lst[i]
        count: int = i + 1

print(max_)
print(count)
