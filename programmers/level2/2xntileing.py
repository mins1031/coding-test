def sol(n) :
    tiles = [1, 2]

    for i in range(2, n):
        temp_value = tiles[-1] + tiles[-2]
        tiles.append(temp_value)

    return tiles[-1]

n = int(input())
print(sol(n))