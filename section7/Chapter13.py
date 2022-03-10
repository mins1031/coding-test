import sys
from collections import deque

sys.stdin = open("in_out/chapter13/in5.txt", "rt")

def bfs(start):
    q = deque([start])
    island[start[0]][start[1]] = 0
    while q:
        now = q.popleft()
        for mx, my in move:
            nx, ny = now[0] + mx, now[1] + my
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if island[nx][ny] == 1:
                q.append((nx, ny))
                island[nx][ny] = 0

if __name__ == "__main__":
    n = int(input())
    island = [list(map(int, input().split())) for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, 1),(1, -1), (1, 1)]
    res = 0
    for i in range(n):
        for j in range(n):
            if island[i][j] == 1:
                bfs((i,j))
                res += 1
    print(res)
