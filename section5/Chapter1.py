import sys

# sys.stdin = open("in_out/chapter1/in1.txt", "rt")


n, m = input().split()

n = list(map(int, n))
m = int(m)

temp = [0]
lt = 0

while len(temp) < m:
    if lt == len(n):
        break

    if temp[-1] < n[lt]:
        temp.pop()
        temp.append(n[lt])
        lt += 1
        continue
    temp.append(n[lt])
    lt += 1

print(str(temp))
