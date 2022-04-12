import sys

n = int(sys.stdin.readline().rstrip())
array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
if n > 1:
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0] + array[0][0]
    dp[1][1] = array[1][1] + array[0][0]

    for i in range(2, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + array[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + array[i][j]
            else:
                dp[i][j] = max(dp[i-1][j] + array[i][j], dp[i-1][j-1] + array[i][j])

    print(max(dp[-1]))

else:
    print(array[0][0])

