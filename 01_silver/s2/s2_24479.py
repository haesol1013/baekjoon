# 알고리즘 수업 - 깊이 우선 탐색 1 - 24479

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


order = 1
def dfs(v):
    global order
    visited[v] = order
    order += 1
    for i in g[v]:
        if not visited[i]:
            dfs(i)


n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in g[1:]:
    i.sort()

dfs(r)

print(*visited[1:], sep="\n")
