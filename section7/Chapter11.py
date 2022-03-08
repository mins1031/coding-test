import sys

sys.stdin = open("in_out/chapter11/in5.txt", "rt")

def dfs(pre_point):
    global res
    if pre_point[0] == maxx and pre_point[1] == maxy:
        res += 1
    else:
        pre_val = mountain[pre_point[0]][pre_point[1]]
        for mx, my in move:
            nx, ny = pre_point[0] + mx, pre_point[1] + my
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and mountain[nx][ny] > pre_val:
                visited[nx][ny] = 1
                dfs((nx, ny))
                visited[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    mountain = []
    visited = [[0] * n for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        mountain.append(list(map(int, input().split())))

    min_val = min(map(min, mountain))
    max_val = max(map(max, mountain))
    minx, miny = 0, 0
    maxx, maxy = 0, 0

    for i in range(n):
        for j in range(n):
            if mountain[i][j] == min_val:
                minx, miny = i, j
            if mountain[i][j] == max_val:
                maxx, maxy = i, j
    res = 0
    dfs((minx, miny))
    print(res)

# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
