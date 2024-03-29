import sys


def mix(box, num1, num2):
    save = box[num1-1]
    box[num1-1] = box[num2-1]
    box[num2-1] = save
    return box


N, M = map(int, sys.stdin.readline().split())
box_gbl = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    box_gbl = mix(box_gbl, i, j)

print(box_gbl)