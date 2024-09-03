# 바이러스 - 2606

import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(v: int) -> None:
    for curr_v in graph[v]:
        if not visited[curr_v]:
            visited[curr_v] = 1
            dfs(curr_v)


def main():
    n = int(input())
    m = int(input())

    global graph, visited
    graph = [[] for _ in range(0, n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = 1
    dfs(1)
    print(sum(visited)-1)


main()
