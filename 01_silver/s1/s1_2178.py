# 미로 탐색 - 2178

from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(g):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0)])
    visit[0][0] = 1
    dxs = [0, -1, 0, 1]
    dys = [1, 0, -1, 0]
    while queue:
        curr_x, curr_y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            if in_range(nx, ny) and not visit[nx][ny] and g[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                g[nx][ny] = g[curr_x][curr_y] + 1
    return g[-1][-1]


n, m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]
ans = bfs(g)
print(ans)
