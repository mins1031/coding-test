import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = 1
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for mx, my in move:
        nx, ny = x + mx, y + my
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if visited[nx][ny] == 0 and baechoo[nx][ny] == 1:
            dfs(nx, ny)

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    baechoo = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    res = 0
    for j in range(k):
        x, y = map(int, input().split())
        baechoo[y][x] = 1

    for x in range(n):
        for y in range(m):
            if baechoo[x][y] == 1 and visited[x][y] == 0:
                dfs(x, y)
                res += 1
    print(res)
