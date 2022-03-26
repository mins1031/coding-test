import sys

n = int(sys.stdin.readline().rstrip())
rgb = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    one, two, three = map(int, sys.stdin.readline().rstrip().split(' '))
    rgb[i][0] = one
    rgb[i][1] = two
    rgb[i][2] = three

sum = min(rgb[0])
standard = rgb[0].index(sum)

# 실패
for i in range(1, n):
    tmp = 1005
    for j in range(3):
        if j == standard:
            continue
        if tmp > rgb[i][j]:
            tmp = rgb[i][j]
            standard = j
    sum += tmp

print(sum)