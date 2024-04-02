import sys


t = int(input())
matrix = [[0 for _ in range(100)] for _ in range(100)]

for i in range(t):
    column, row = map(int, sys.stdin.readline().split())
    for r in range(row-1, row+9):
        for c in range(column-1, column+9):
            matrix[r][c] = 1

area = 0
for j in matrix:
    area += sum(j)
print(area)
