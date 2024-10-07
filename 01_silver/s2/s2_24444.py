# 알고리즘 수업 - 너비 우선 탐색 1 - 24444

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(v):
    queue = deque([v])
    order = 1
    visit[v] = order
    while queue:
        curr_v = queue.popleft()
        for next_v in g[curr_v]:
            if not visit[next_v]:
                order += 1
                visit[next_v] = order
                queue.append(next_v)


n, m, r = map(int, input().split())
g: list[list[int]] = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in g:
    i.sort()

bfs(r)

print(*visit[1:], sep="\n")





