import sys
from collections import deque

def bfs(start, step):
    q = deque([start])
    while q:
        now = q.popleft()
        ch[now[0]][now[1]] = 1
        for tx, ty in move:
            nx, ny = now[0] + tx, now[1] + ty
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if region[nx][ny] > step and ch[nx][ny] == 0:
                q.append((nx, ny))
                ch[nx][ny] = 1


n = int(input())
region = []

for _ in range(n):
    region.append(list(map(int, sys.stdin.readline().rstrip().split())))
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_dis = max(map(max, region))
res = []

for i in range(1, max_dis):
    stand = 0
    ch = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if region[j][k] > i and ch[j][k] == 0:
                bfs((j,k), i)
                stand += 1
    res.append(stand)
res.append(1)

print(max(res))
