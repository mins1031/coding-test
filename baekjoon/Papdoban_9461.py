import sys

test = int(sys.stdin.readline().rstrip())
res = []
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    dy = [1, 1, 1, 2, 2]

    for i in range(5, n):
        dy.append(dy[i - 2] + dy[i - 3])

    res.append(dy[n - 1])

for i in res:
    print(i)
