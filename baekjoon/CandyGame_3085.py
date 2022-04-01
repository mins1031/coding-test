import sys

n = int(sys.stdin.readline().rstrip())
board = []
for i in range(n):
    k = sys.stdin.readline().rstrip()
    board.append(list(k))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []

for i in range(n):
    for j in range(n):
        tmp = board[i][j]
        if j < n-1 and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp_cnt = 0
            for k in range(1, n):
                if board[i][k] == board[i][k-1]:
                    tmp_cnt += 1
                else:
                    tmp_cnt = 0
            res.append(tmp_cnt)

            tmp_cnt = 0
            for k in range(1, n):
                if board[k][j] == board[k-1][j]:
                    tmp_cnt += 1
                else:
                    tmp_cnt = 0
            res.append(tmp_cnt)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i < n-1 and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp_cnt = 0
            for k in range(1, n):
                if board[i][k] == board[i][k-1]:
                    tmp_cnt += 1
                else:
                    tmp_cnt = 0
            res.append(tmp_cnt)

            tmp_cnt = 0
            for k in range(1, n):
                if board[k][j] == board[k-1][j]:
                    tmp_cnt += 1
                else:
                    tmp_cnt = 0
            res.append(tmp_cnt)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max(res))

