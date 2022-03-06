from collections import deque


def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if not visited[v] :
            visited[v] = True
            print(v, end=" ")
            for i in graph[v]:
                q.append(i)

    return visited


def dfs(L):
    print(L, end=' ')
    visited[L] = True
    for i in graph[L]:
        if not(visited[i]):
            dfs(i)


n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

visited = [False] * (n+1)
dfs(start)
print()
visited = [False] * (n+1)
bfs(start)