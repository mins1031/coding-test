import sys


# sys.stdin = open("in_out/chapter15/in1.txt", "rt")


def bfs(now):
    ch[now[0]][now[1]] = 1
    for mx, my in move:
        nx, ny = now[0] + mx, now[1] + my
        if nx < 0 or nx >= m or ny < 0 or ny >= n or tomatos[nx][ny] == -1:
            continue
        if ch[nx][ny] == 0 and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(m)]
    ch = [[0] * n for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    res = 1000

    point = []
    for i in range(m):
        for j in range(n):
            if tomatos[i][j] == 1:
                point.append(tomatos[i][j])

    print(point)

    print(res)
