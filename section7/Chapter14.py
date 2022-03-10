import sys
from collections import deque

# sys.stdin = open("in_out/chapter14/in1.txt", "rt")


def bfs(start, rain):
    q = deque([start])
    while q:
        now = q.popleft()
        for mx, my in move:
            nx, ny = now[0] + mx, now[1] + my
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if region[nx][ny] > rain and ch[nx][ny] == 0:
                q.append((nx, ny))
                dis[nx][ny] = dis[now[0]][now[1]] + 1
                ch[now[0]][now[1]] = 1

    max_dis = max(map(max, dis))
    res.append(max_dis)

if __name__ == "__main__":
    n = int(input())
    region = [list(map(int, input().split())) for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []
    max_val = max(map(max, region))
    for k in range(max_val):
        dis = [[0] * n for _ in range(n)]
        ch = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if region[i][j] > k and ch[i][j] == 0:
                    bfs((i, j), k)

    print(max(res))

# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7