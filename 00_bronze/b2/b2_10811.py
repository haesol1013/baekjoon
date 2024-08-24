import sys


def mix(bundle, start, end):
    mixing = [i for i in bundle[start-1:end]]
    mixing.reverse()
    bundle[start-1:end] = mixing
    return bundle


N, M = map(int, sys.stdin.readline().split())
box = [k for k in range(1, N+1)]

for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    box = mix(box, i, j)

for k in box:
    print(k, end=' ')

print("hello git")