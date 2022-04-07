import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    dp = [0,1,1,3,3,4]
    n = int(sys.stdin.readline().strip())
    target = 3
    if n <= 5 :
        print(dp[n])
    else:
        for i in range(5, n):
            if i % 5 == 3:
                dp[i] = dp[i-1] -1
                continue
            else:
                dp[i] = dp[i-2] * target

print(dp)


