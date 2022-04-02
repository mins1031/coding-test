import sys

def row(row):
    tmp = 1
    res = 1
    for i in range(1, n):
        if board[row][i] == board[row][i - 1]:
            tmp += 1
        else:
            tmp = 1
    if res < tmp :
        res = tmp
    return res


def col(col):
    tmp = 1
    res = 1
    for i in range(1, n):
        if board[i][col] == board[i - 1][col]:
            tmp += 1
        else:
            tmp = 1
    if res < tmp :
        res = tmp

    return res


n = int(sys.stdin.readline().rstrip())
board = []
for i in range(n):
    k = sys.stdin.readline().rstrip()
    board.append(list(k))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []

for i in range(n):
    res.append(row(i))

for i in range(n):
    res.append(col(i))

for i in range(n):
    for j in range(n):
        tmp = board[i][j]
        if j +1 < n:
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = tmp
            res.append(row(i))
            res.append(col(i))
            board[i][j + 1] = board[i][j]
            board[i][j] = tmp
        if i+1 < n:
            board[i][j] = board[i+1][j]
            board[i+1][j] = tmp
            res.append(row(i))
            res.append(col(i))
            board[i + 1][j] = board[i][j]
            board[i][j] = tmp

print(max(res))
