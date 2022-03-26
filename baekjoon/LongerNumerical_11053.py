import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
dy = [0] * n

dy[0] = 1
for i in range(1, n):
    tmp_max = 0

    for j in range(i-1, -1, -1):
        if a[i] > a[j]:
            if dy[j] > tmp_max:
                tmp_max = dy[j]
    dy[i] = tmp_max + 1

print(max(dy))