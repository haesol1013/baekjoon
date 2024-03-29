import sys


def put(bundle, start, end, num):
    stand_by = [i for i in bundle[start-1:end]]

    for i in range(len(stand_by)):
        stand_by[i] = num

    bundle[start-1:end] = stand_by
    return bundle


N, M = map(int, sys.stdin.readline().split())
box = [0 for _ in range(N)]

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    box = put(box, i, j, k)

for x in box:
    print(x, end=' ')
