import sys
from collections import deque


# sys.stdin = open("in_out/chapter8/in5.txt", "rt")

def bfs():
    q = deque()
    q.append((0,0))
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        now = q.popleft()
        visited[now[0]][now[1]] = 1
        for x,y in move:
            nx, ny = now[0] + x, now[1] + y
            if nx < 0 or nx > 6 or ny < 0 or ny > 6:
                continue
            if visited[nx][ny] == 0 and miro[nx][ny] == 0:
                q.append((nx, ny))
                dis[nx][ny] = dis[now[0]][now[1]] + 1


if __name__ == "__main__":
    miro = [list(map(int, input().split())) for _ in range(7)]
    dis = [[0] * 7 for _ in range(7)]
    visited = [[0] * 7 for _ in range(7)]

    bfs()
    print(dis[6][6])

# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0

