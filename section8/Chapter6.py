# import sys
#
# sys.stdin = open("in_out/chapter6/in5.txt", "rt")

n = int(input())
brick = []

for i in range(n):
    tmp = list(map(int, input().split(' ')))
    brick.append((tmp[0], tmp[1], tmp[2], i))

brick.sort(reverse=True)
dy = [0] * n
dy[0] = brick[0][1]
idx = []
idx.append((1, brick[0][3]))
for i in range(1, n):
    tmp_max = 0
    tmp_idx = []
    cnt = 1
    for j in range(i - 1, -1, -1):
        if brick[i][2] < brick[j][2] and dy[j] > tmp_max:
            tmp_max = dy[j]
            cnt += 1
            tmp_idx.append(brick[j][3])
    dy[i] = tmp_max + brick[i][1]
    idx.append((cnt, tmp_idx))

res = dy.index(max(dy))
print(max(dy))
print(idx)
print(dy.index(max(dy)))
print(idx[res])

