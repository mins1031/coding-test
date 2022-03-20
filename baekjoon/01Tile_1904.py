n = int(input())
tiles = [0] * n
tiles[0] = 1
tiles[1] = 2

for i in range(2, n):
    tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746

print(tiles[n-1])