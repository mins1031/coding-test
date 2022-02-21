from collections import deque


def bfs(graph, start_node):
    visited = deque()
    need_visit = deque()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


def dfs(graph, start_node):
    visited = deque()
    need_visit = deque()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


n, m, start = map(int, input().split())
graph = dict()

for i in range(m):
    k, v = map(int, input().split())
    if k in graph:
        graph[k].append(v)
    else:
        graph[k] = [v]

    if v in graph:
        graph[v].append(k)
    else:
        graph[v] = [k]

print(graph)
dfs_result = dfs(graph, start)
bfs_result = bfs(graph, start)

for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')
