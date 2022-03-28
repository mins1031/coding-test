import sys
from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for tx, ty in move:
            nx, ny = now[0] + tx, now[1] + ty
            if nx < 0 or nx >= height or ny < 0 or ny >= weight:
                continue
            if island[nx][ny] == 1 and ch[nx][ny] == 0:
                q.append((nx, ny))
                ch[nx][ny] = 1

while True:
    weight, height = map(int, sys.stdin.readline().rstrip().split(' '))
    if weight == 0 and height == 0:
        break
    island = []

    for _ in range(height):
        island.append(list(map(int, sys.stdin.readline().rstrip().split())))

    move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1),(1, -1), (1, 1)]
    ch = [[0 for _ in range(weight)] for _ in range(height)]
    res = 0
    for i in range(height):
        for j in range(weight):
            if island[i][j] == 1 and ch[i][j] == 0:
                bfs((i,j))
                res += 1

    print(res)






