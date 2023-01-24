import sys

n = int(input())
candy_board = []
same_candy_max_count = 1

def height():
    global same_candy_max_count

    same_candy_count = 1
    for wid in range(n):
        for hei in range(1, n):
            if candy_board[hei][wid] == candy_board[hei-1][wid]:
                same_candy_count += 1
                same_candy_max_count = max(same_candy_count, same_candy_max_count)
            else:
                same_candy_count = 1
        same_candy_count = 1

def wight():
    global same_candy_max_count

    same_candy_count = 1
    for hei in range(n):
        for wid in range(1, n):
            if candy_board[hei][wid] == candy_board[hei][wid - 1]:
                same_candy_count += 1
                same_candy_max_count = max(same_candy_count, same_candy_max_count)
            else:
                same_candy_count = 1
        same_candy_count = 1

for i in range(n):
    k = sys.stdin.readline().rstrip()
    candy_board.append(list(k))

for i in range(1, n):
    for j in range(1, n):
        if candy_board[i][j] != candy_board[i][j-1] :
            candy_board[i][j], candy_board[i][j - 1] = candy_board[i][j-1], candy_board[i][j]
            height()
            wight()
            candy_board[i][j], candy_board[i][j - 1] = candy_board[i][j-1], candy_board[i][j]
        if candy_board[i][j] != candy_board[i-1][j] :
            candy_board[i][j], candy_board[i-1][j] = candy_board[i-1][j], candy_board[i][j]
            height()
            wight()
            candy_board[i][j], candy_board[i-1][j] = candy_board[i-1][j], candy_board[i][j]

print(same_candy_max_count)

'''
정말 단순하게 
'''