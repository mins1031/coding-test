def solution(board):
    answer = 0
    row_leng = len(board[0])
    col_leng = len(board)
    for i in range(col_leng):
        for j in range(row_leng):
            if board[i][j] == 1:
                tmp_i = i
                tmp_j = j
                tmp_bigger = 1
                while True:
                    tmp_i += 1
                    tmp_j += 1
                    if tmp_j >= row_leng or tmp_i >= col_leng:
                        break
                    if board[i][tmp_j] != 1 or board[tmp_i][j] != 1 or board[tmp_i][tmp_j] != 1:
                        break
                    tmp_bigger += 1
                if answer < tmp_bigger + 1:
                    answer = tmp_bigger

    return answer ** 2

#실패
board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board2 = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))
print(solution(board2))
