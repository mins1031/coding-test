import sys

n = int(input())
dp = [0] * (n+1)
day = [0] * (n+1)
value = [0] * (n+1)
for i in range(1, n+1):
    k, m = map(int, input().split())
    day[i] = k
    value[i] = m

for i in range(1, n+1):
    if day[i] + i > n:
        continue
    else:
        dp[i] += value[i]
        for j in range(i+day[i], n+1):
            dp[j] = max(dp[j], dp[i])
print(dp)