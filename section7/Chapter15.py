import sys
from collections import deque


sys.stdin = open("in_out/chapter15/in2.txt", "rt")

def bfs(q):
    while q:
        now = q.popleft()
        for mx, my in move:
            nx, ny = now[0] + mx, now[1] + my
            if nx < 0 or nx >= m or ny < 0 or ny >= n or tomatos[nx][ny] == -1:
                continue
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = 1
                dis[nx][ny] = dis[now[0]][now[1]] + 1
                q.append((nx,ny))


if __name__ == "__main__":
    n, m = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(m)]
    dis = [[0] * n for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    res = 0
    q = deque()
    # 초기값 1의 위치를 전달하기 위해 2차원배열을 뒤지며 1의 좌표를 찾아냄
    for i in range(m):
        for j in range(n):
            if tomatos[i][j] == 1:
                q.append((i,j))

    # 이후론 bfs를 돌며 차례로 적용됨.
    bfs(q)
    flag = 1
    for i in range(m):
        for j in range(n):
            if tomatos[i][j] == 0:
                flag = 0

    if flag == 1:
        for i in range(m):
            for j in range(n):
                if dis[i][j] > res:
                    res = dis[i][j]
        print(res)
    else:
        print(-1)