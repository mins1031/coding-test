n = int(input())
line = list(map(int, input().split()))

line.sort()
sum_t = 0
res = []
for i in range(n):
    sum_t += line[i]
    res.append(sum_t)

print(sum(res))