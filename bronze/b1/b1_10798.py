import sys


matrix = [[] for _ in range(5)]
for i in range(5):
    matrix[i] = [j for j in list(sys.stdin.readline().strip())]

max_len = 0
for i in range(5):
    partial_len = len(matrix[i])
    if partial_len > max_len:
        max_len = partial_len

for i in range(5):
    partial_len = len(matrix[i])
    diff = max_len - partial_len
    if diff > 0:
        matrix[i] += ['' for _ in range(diff)]

for i in range(max_len):
    for j in range(5):
        print(matrix[j][i], end='')
