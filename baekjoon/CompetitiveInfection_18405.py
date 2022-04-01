import sys
from collections import deque

def bfs(start, p):
    q = deque([start])
    while q:
        now = q.popleft()
        for mx, my in move:
            nx, ny = now[0] + mx, now[1] + my
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if sub[nx][ny] > sub[now[0]][now[1]] or sub[nx][ny] == 0:
                if ch[nx][ny] == p or ch[nx][ny] == 0:
                    sub[nx][ny] = sub[now[0]][now[1]]
                    ch[nx][ny] = p


n, k = map(int, sys.stdin.readline().rstrip().split())
sub = []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ch = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    sub.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        if sub[i][j] != 0 :
            ch[i][j] = 1

s, x, y = map(int, sys.stdin.readline().rstrip().split())

for p in range(1, s+1):
    for i in range(n):
        for j in range(n):
            if sub[i][j] != 0 :
                bfs((i, j), p)

print(sub[x-1][y-1])

# and ch[i][j] < p