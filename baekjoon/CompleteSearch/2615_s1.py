def find_omok(now_x, now_y, color):
    global board, board_check, n
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    omok_success = False
    for x, y in directions:
        if (now_x + x) >= n or (now_y + y) >= n:
            break
        if board[now_x + (x * -1)][now_y + (y * -1)] == color:
            continue

        temp_x = now_x + x
        temp_y = now_y + y
        if board[temp_x][temp_y] == color and board_check[temp_x][temp_y] == 0:
            for i in range(4):
                temp_x += x
                temp_y += y
                if board[temp_x][temp_y] == color and board_check[temp_x][temp_y] == 0:
                    continue
                else:
                    break
            else:
                if board[temp_x + x][temp_y + y] == color:
                    omok_success = False
                else:
                    omok_success = True

        if omok_success:
            break

    return omok_success

n = 19
board = []
board_check = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp_row = list(map(int, input().split()))
    board.append(temp_row)

target_x = 0
target_y = 0
winner = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            is_omok = find_omok(i, j, board[i][j])
            if is_omok:
                winner = board[i][j]
                target_x = i + 1
                target_y = j + 1

        if winner != 0 :
            break
        board_check[i][j] = 1

    if winner != 0:
        break

print(winner)
print(target_x, end=' ')
print(target_y)
