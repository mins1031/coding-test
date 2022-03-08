import sys
from collections import deque

sys.stdin = open("in_out/chapter12/in1.txt", "rt")

def bfs(start, cnt):
    q = deque([start])
    ch[start[0]][start[1]] = 1
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    roop_cnt = 0
    while q:
        now = q.popleft()
        roop_cnt += 1
        for mx,my in move:
            nx, ny = now[0] + mx, now[1] + my
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dange[nx][ny] == 1 and ch[nx][ny] == 0:
                q.append((nx, ny))
                ch[nx][ny] = 1
    cnt_list.append(roop_cnt)
    cnt + 1

if __name__ == "__main__":
    n = int(input())
    dange = [list(map(int, input())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]

    cnt = 0
    cnt_list = []
    for i in range(n):
        for j in range(n):
            if dange[i][j] == 1 and ch[i][j] == 0:
                bfs((i,j), cnt)
                cnt += 1
    print(cnt)
    cnt_list.sort()
    for i in cnt_list:
        print(i)



# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000