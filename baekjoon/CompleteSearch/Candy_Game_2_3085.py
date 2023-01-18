import sys

def check(arr, x, y) :
    count = len(arr)
    biggest = 1
    temp_cnt = 1

    for i in range(1, count) :
        if arr[i][y] == arr[i-1][y] :
            temp_cnt += 1
        else:
            temp_cnt = 1

    if biggest < temp_cnt:
        biggest = temp_cnt

    temp_cnt = 1
    for i in range(1, count):
        if arr[x][i] == arr[x][i - 1]:
            temp_cnt += 1
        else:
            temp_cnt = 1

    if biggest < temp_cnt :
        biggest = temp_cnt

    return biggest

n = int(sys.stdin.readline())
board = []
result = 0

for i in range(n):
    one_row = input()
    board.append(list(one_row))

for i in range(n):
    for j in range(n):
        temp = 0
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board, i, j)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if temp > result :
            result = temp

        temp = 0

        if i+1 < n :
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board, i, j)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

        if temp > result :
            result = temp

print(result)



