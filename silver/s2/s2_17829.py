

def pooling(matrix):
    while len(matrix[0]) > 1:
        new_matrix = []

        for row in range(0, len(matrix), 2):
            tmp_row = []

            for col in range(0, len(matrix), 2):
                calc = sorted([matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]])
                tmp_row.append(calc[2])
            new_matrix.append(tmp_row)

        matrix = new_matrix[:]
    return matrix[0][0]


n = int(input())
matrix_out = [list(map(int, input().split())) for _ in range(n)]
print(pooling(matrix_out))
print(type(n))