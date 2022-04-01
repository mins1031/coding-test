n = int(input())
dungchi = []
for i in range(n):
    x, y = map(int, input().split())
    dungchi.append((x, y))

res = [1] * n
for i in range(n):
    for j in range(n):
        if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            res[i] += 1

for i in res:
    print(i, end=' ')

