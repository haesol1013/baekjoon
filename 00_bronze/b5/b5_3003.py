input_piece = list(map(int, input().split()))
std_piece = [1, 1, 2, 2, 2, 8]
necessary_piece = [0 for _ in range(6)]

for i in range(6):
    necessary_piece[i] = std_piece[i] - input_piece[i]

print(*necessary_piece)
