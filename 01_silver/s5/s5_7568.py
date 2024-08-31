# 덩치 - 7568

import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    for i in arr:
        rank = 1
        for j in arr:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=" ")


main()
