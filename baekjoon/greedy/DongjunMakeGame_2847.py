import sys

n = int(sys.stdin.readline().rstrip())
level = []
for i in range(n):
    level.append(int(sys.stdin.readline().rstrip()))

res = 0
for i in range(n-2, -1, -1):
    if level[i+1] <= level[i]:
        tmp = (level[i] - level[i+1]) + 1
        level[i] -= tmp
        res += tmp

print(res)
