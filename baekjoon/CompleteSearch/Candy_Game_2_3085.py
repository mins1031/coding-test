import sys

n = int(sys.stdin.readline())
board = []
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 상하좌우
results = []

def swap(exist_x_position, exist_y_position, exist_color) :
    for dir in directions:
        target_x_position = exist_x_position + dir[0]
        target_y_position = exist_y_position + dir[1]
        if target_x_position < 0 or target_x_position >= n :
            continue
        elif target_y_position < 0 or target_y_position >= n :
            continue

        if board[target_x_position][target_y_position] == exist_color :
            continue

        board[exist_x_position][exist_y_position], board[target_x_position][target_y_position] = board[target_x_position][target_y_position], board[exist_x_position][exist_y_position]


def move(exist_x, exist_y, target_x, target_y) :
    overlaps = []
    if exist_y == target_y and exist_x != target_x :
        overlap_count = 0
        for i in range(1, n):
            if board[exist_x][i-1] == board[exist_x][i]:
                overlap_count += 1
            else:
                overlaps.append(overlap_count)
                overlap_count = 0

    elif exist_y != target_y and exist_x == target_x :




for i in range(n):
    one_row = input()
    board.append(list(one_row))



for i in range(n):
    for j in range(n):
        board[i][j]



