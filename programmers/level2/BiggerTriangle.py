'''
정답은 나오나 시간초과되는 로직
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
'''

def solution(board):
    answer = 0
    row_leng = len(board[0])
    col_leng = len(board)
    dp = [[0] * row_leng for _ in range(col_leng)]
    dp[0] = board[0]
    for i in range(1, col_leng):
        dp[i][0] = board[i][0]

    for i in range(1, col_leng):
        for j in range(1, row_leng):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1]) + 1

    for i in range(col_leng):
        bigger = max(dp[i])
        if bigger > answer:
            answer = bigger

    return answer ** 2

#실패
board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board2 = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))
print(solution(board2))
# dp로 풀어야한다고 한다... min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1]) 이 점화식을 도출할수 있어야 하는데 사실 생각조차 못함 ...ㅋㅋㅋ 채점은 안하고 나중에 다시 풀어볼것.
# 저건 1,1 부터 시작하며 2 x 2 사각형을 보며 점점 높혀가는 방식이다. 사각형의 최소값이 도출되는 이유는 최소값이 현재 위치에서 해당 사각형을 만들수 있는 최소 범위이기 때문이다.