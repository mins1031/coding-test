
def solution(board, moves):
    answer = 0
    stack = []
    leng = len(board[0])
    for i in moves:
        for j in range(leng):
            if board[j][i-1] != 0:
                if len(stack) != 0 and stack[-1] == board[j][i-1]:
                    stack.pop()
                    board[j][i-1] = 0
                    answer += 2
                    break
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))