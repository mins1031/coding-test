n = int(input())
stair = [0] * n
stair[0] = 1
stair[1] = 2

for i in range(2, n):
    stair[i] = stair[i - 1] + stair[i - 2]

print(stair[n - 1])