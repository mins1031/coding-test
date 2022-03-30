import sys

n = int(sys.stdin.readline().rstrip())
graph = []
dy = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            dy[i][j] = 1
            continue

        if graph[i][j] == 1:
            dy[i][j] = 1
            dy[j][i] = 1

print(dy)
