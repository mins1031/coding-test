import sys

sys.stdin = open("in_out/chapter9/in5.txt", "rt")

n = int(input())
map_info = [list(map(int, input().split())) for _ in range(n)]

map_info.insert(0, [0] * n)
map_info.append([0] * n)

for i in map_info:
    i.insert(0, 0)
    i.append(0)

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        up = map_info[i][j - 1]
        bottom = map_info[i + 1][j]
        left = map_info[i - 1][j]
        right = map_info[i][j + 1]
        standard = map_info[i][j]
        if standard > up and standard > bottom and standard > left and standard > right:
            cnt += 1

print(cnt)
