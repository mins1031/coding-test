import sys

sys.stdin = open("in_out/chapter10/in5.txt", "rt")

def dfs(now):
    global res
    if now[0] == 6 and now[1] == 6:
        res += 1
    else:
        for x, y in move:
            nx, ny = now[0] + x, now[1] + y
            if nx < 0 or nx > 6 or ny < 0 or ny > 6:
                continue
            if miro[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[now[0]][now[1]] = 1
                dfs((nx, ny))
                visited[now[0]][now[1]] = 0


if __name__ == "__main__":
    miro = [list(map(int, input().split())) for _ in range(7)]
    visited = [[0] * 7 for _ in range(7)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 0
    dfs((0,0))
    print(res)