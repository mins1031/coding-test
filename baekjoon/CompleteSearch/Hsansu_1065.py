import sys

n = int(sys.stdin.readline().rstrip())
res = 0
for i in range(1, n + 1):
    if i < 100:
        res += 1
        continue
    else:
        tmp = str(i)
        if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
            res += 1
print(res)

