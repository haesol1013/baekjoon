# 유기농 배추 - 1012

import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(x: int, y: int) -> None:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and graph[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny))


def in_range(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < m


def main():
    t = int(input())
    for _ in range(t):
        global graph, visited, m, n

        m, n, k = map(int, input().split())

        graph = [[0]*m for _ in range(n)]
        visited = [[0]*m for _ in range(n)]
        for _ in range(k):
            y, x = map(int, input().split())
            graph[x][y] = 1

        result = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] and not visited[i][j]:
                    result += 1
                    dfs(i, j)
        print(result)


if __name__ == "__main__":
    main()