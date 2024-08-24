import sys

N, M = map(int, sys.stdin.readline().split())
box = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    box[i], box[j] = box[j], box[i]

box.pop(0)
print(' '.join(map(str, box)))
