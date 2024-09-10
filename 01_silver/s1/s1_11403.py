# 경로 찾기 - 11403

import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    for m in range(n):
        for i in range(n):
            for j in range(n):

                if graph[i][m] and graph[m][j]:
                    graph[i][j] = 1

                print(f"{i = }, {m = }, {j = }")
                for k in graph:
                     print(*k)
                print()



if __name__ == "__main__":
    main()
