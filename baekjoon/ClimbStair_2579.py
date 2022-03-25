import sys

n = int(sys.stdin.readline().strip())
stair = [0] * (n+1)
for i in range(1, n+1):
    stair[i] = int(sys.stdin.readline().strip())

t1 = [0] * (n+1)
t2 = [0] * (n+1)
dp = [0] * (n+1)
t1[1] = 0
t2[1] = stair[1]

for i in range(2, n+1):
    t1[i] = t2[i-1] + stair[i]
    t2[i] = max(t1[i-2], t2[i-2]) + stair[i]

print(max(t1[n], t2[n]))
