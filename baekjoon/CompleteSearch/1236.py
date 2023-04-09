row, col = map(int, input().split())
castle = []

for i in range(row):
    temp_col = list(str(input()))
    castle.append(temp_col)

row_count = 0
col_count = 0

for i in range(row):
    for j in range(col):
        if castle[i][j] == "X":
            break
    else:
        row_count += 1

for i in range(col):
    for j in range(row):
        if castle[j][i] == "X":
            break
    else:
        col_count += 1

if row_count >= col_count:
    print(row_count)
else:
    print(col_count)


