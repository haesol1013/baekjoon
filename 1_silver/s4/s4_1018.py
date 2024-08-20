# 체스판 다시 칠하기 - 1018

import sys

input = lambda: sys.stdin.readline().rstrip()


def get_local_min(board: list[str], start_x: int, start_y: int) -> int:
    cnt_w = 0
    cnt_b = 0

    for x in range(start_x, start_x + 8):
        for y in range(start_y, start_y + 8):
            curr_color = board[x][y]
            if (x + y) % 2 == 0:
                if curr_color == "W":
                    cnt_w += 1
                else:
                    cnt_b += 1
            else:
                if curr_color == "W":
                    cnt_b += 1
                else:
                    cnt_w += 1

    return min(cnt_w, cnt_b)


def get_global_min(board: list[str], n: int, m: int) -> int:
    min_cnt = float('inf')

    for start_x in range(n - 7):
        for start_y in range(m - 7):
            curr_cnt = get_local_min(board, start_x, start_y)
            min_cnt = min(min_cnt, curr_cnt)

    return min_cnt


def main():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    cnt = get_global_min(matrix, n, m)
    print(cnt)


main()
