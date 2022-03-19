n = int(input())

tile = [1, 3, 5]
for i in range(3, n):
    tile.append(tile[i - 1] + (tile[i - 2]* 2))

print(tile[n - 1] % 10007)
