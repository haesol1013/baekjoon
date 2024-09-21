# DFS와 BFS - 1260

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m, v = map(int, input().split())
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in g:
        i.sort()

    visit = [False] * (n+1)
    dfs(g, visit, v)
    print()

    visit = [False] * (n+1)
    bfs(g, visit, v)


def dfs(g, visit, v):
    visit[v] = True
    print(v, end=" ")

    for i in g[v]:
        if not visit[i]:
            visit[i] = True
            dfs(g, visit, i)


def bfs(g, visit, v):
    queue = deque([v])
    visit[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in g[v]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)


main()
