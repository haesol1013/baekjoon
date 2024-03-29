import sys


N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print('')
