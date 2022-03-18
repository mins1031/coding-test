import sys
n, m = map(int, sys.stdin.readline().split())

chae = [True] * (m+1)
chae[0] = False
chae[1] = False

for i in range(2, m + 1):
    if chae[i] == True:
        for j in range(i + i, m+1, i):
            chae[j] = False

for i in range(n, m + 1):
    if chae[i] == True:
        print(i)

